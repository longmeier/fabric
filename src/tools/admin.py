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
    list_display = ('id', 'name', 'user_name', 'ip', 'git_url', 'status', 'by_user', 'memo')
    actions = ('deploy_project', 'check_info')
    ordering = ['-id']

    def check_info(self, request, queryset):
        qs = queryset[0]
        ssh_user = qs.user_name
        ssh_ip = qs.ip
        tmp_code_path = qs.tmp_code_path
        message_bit, ssh_flag, git_flag = '', False, False
        if qs.flag == 1:
            ssh_pwd = settings.TST_PWD
        elif qs.flag == 2:
            ssh_pwd = settings.PRD_PWD
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
        qs = queryset.all()

        message_bit = '%s 条客户审核通过，%s未审核过(证明不全/状态不对)'

        self.message_user(request, '%s' % message_bit)

    deploy_project.short_description = '一键发布'