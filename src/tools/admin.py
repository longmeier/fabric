from django.contrib import admin
from .models import Settings, DeployLog
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
    list_display_links = ['id', 'name', 'user_flag', 'ip', 'git_url', 'status', 'by_user', 'memo']
    exclude = ('by_user',)
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
                con.run('rm -rf ' + git_name)
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
        user_flag = qs.user_flag
        ssh_ip = qs.ip
        code_path = qs.code_path
        before_cmd = qs.before_cmd
        before_list = before_cmd.split('\r\n')
        after_cmd = qs.after_cmd
        after_list = after_cmd.split('\r\n')
        log_str, log_status = '', 0
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
        try:
            # 连接服务器
            con = Connection(ssh_user+'@'+ssh_ip, connect_kwargs={'password': ssh_pwd})
            log_str += '1.连接服务器'
            git_url = qs.git_url
            git_list = git_url.split('/')
            git_name = git_list[-1]
            if '.' in git_name:
                git_name = git_name.split('.')[0]
            log_str += '2.获取git项目名称'
            # 检测git连接
            with con.cd(code_path + '/' + git_name):
                log_str += '3.进入目标路径'
                for before_line in before_list:
                    if before_line:
                        con.run(before_line)
                log_str += '4.执行拉取前的操作'
                con.run('git pull')
                log_str += '5.拉取代码'
                for after_line in after_list:
                    if after_line:
                        con.run(after_line)
                log_str += '6.执行拉取后的操作'
                message_bit = '发布成功...'
                log_status = 1
        except Exception as e:
            log.info('发布出错error:%s', str(e))
            log_str += 'error:%s' % str(e)
            message_bit = '发布失败，详情请查看日志。'
        DeployLog.objects.create(by_user=request.user, content=log_str, status=log_status)
        self.message_user(request, '%s' % message_bit)

    deploy_project.short_description = '一键发布'

    def response_post_save_add(self, request, obj):
        user = request.user
        obj.by_user = user  # 添加人
        obj.save()
        return super(SettingsAdmin, self).response_post_save_add(request, obj)


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    search_fields = ('by_user', 'status')
    list_display = ('id', 'by_user', 'content', 'status')
    list_display_links = ['id', 'by_user', 'content', 'status']
    exclude = ('by_user',)
    ordering = ['-id']


admin.site.disable_action('delete_selected')