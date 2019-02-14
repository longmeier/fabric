from django.contrib import admin
from .models import Settings
import datetime
from fabric import Connection
from django.conf import settings
import os

import logging
log = logging.Logger(__name__)

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    search_fields = ('name', 'status')
    list_display = ('id', 'name', 'user_flag', 'ip', 'git_url', 'status', 'by_user', 'memo')
    actions = ('check_info', 'deploy_project', )
    ordering = ['-id']

    def check_info(self, request, queryset):
        qs = queryset[0]
        user_flag = qs.user_flag
        # pyer用户
        if user_flag == 1:
            ssh_user = 'pyer'
            # 测试环境
            if qs.flag == 1:
                ssh_pwd = settings.TST_PYER_PWD
                # 生产环境
            elif qs.flag == 2:
                ssh_pwd = settings.PRD_PYER_PWD
        # root 用户
        elif user_flag == 2:
            ssh_user = 'root'
            if qs.flag == 1:  # 测试环境
                ssh_pwd = settings.TST_ROOT_PWD
            elif qs.flag == 2:  # 生产环境
                ssh_pwd = settings.PRD_ROOT_PWD

        ssh_ip = qs.ip
        tmp_code_path = qs.tmp_code_path
        message_bit, ssh_flag, git_flag = '', False, False

        try:
            # 连接服务器
            con = Connection(ssh_user+'@'+ssh_ip, connect_kwargs={'password': ssh_pwd})
            git_url = qs.git_url
            # 检测git连接
            with con.cd(tmp_code_path):
                git_list = git_url.split('/')
                git_name = git_list[-1]
                if '.' in git_name:
                    git_name = git_name.split('.')[0]
                # if not os.path.exists(tmp_code_path + '/' + git_name):
                #     con.run('mkdir ' + git_name)
                # else:
                con.run('rm -rf ' + git_name)
                # if user_flag == 2:
                #     con.run('su pyer')
                res = con.run('git clone ' + git_url)
                git_flag = True
                message_bit += '2.' + res.stdout
            ret = con.is_connected
            if ret:
                log.info('1.连接服务器成功....')
                ssh_flag = True
        except Exception as e:
            log.info('检查配置出错error:%s', str(e))
        if ssh_flag and git_flag:
            message_bit = '服务器连接正常'
        else:
            message_bit = '服务器连接异常，请查看日志'
        self.message_user(request, '%s' % message_bit)

    check_info.short_description = '检查配置信息'

    def deploy_project(self, request, queryset):
        qs = queryset[0]
        ssh_user = qs.user_name
        ssh_ip = qs.ip
        code_path = qs.code_path
        before_cmd = qs.before_cmd
        before_list = before_cmd.split('\r\n')
        after_cmd = qs.after_cmd
        after_list = after_cmd.split('\r\n')
        message_bit = '未发布'
        if qs.flag == 1:
            ssh_pwd = settings.TST_PWD
        elif qs.flag == 2:
            ssh_pwd = settings.PRD_PWD
        try:
            # 连接服务器
            con = Connection(ssh_user+'@'+ssh_ip, connect_kwargs={'password': ssh_pwd})
            git_url = qs.git_url
            git_list = git_url.split('/')
            git_name = git_list[-1]
            if '.' in git_name:
                git_name = git_name.split('.')[0]
            # 检测git连接
            with con.cd(code_path + '/' + git_name):
                for before_line in before_list:
                    if before_line:
                        con.run(before_line)
                con.run('git pull')
                for after_line in after_list:
                    if after_line:
                        con.run(after_line)
                message_bit = '发布成功...'
        except Exception as e:
            log.info('发布出错error:%s', str(e))
            message_bit = '发布失败，详情请查看日志。'

        self.message_user(request, '%s' % message_bit)

    deploy_project.short_description = '一键发布'