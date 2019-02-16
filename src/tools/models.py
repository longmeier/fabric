from django.db import models
from django.db.models import Q
import datetime
from model_utils.models import TimeStampedModel
from users.models import User

# Create your models here.


class Settings(TimeStampedModel):
    """
    配置表
    """

    class Meta:
        verbose_name = verbose_name_plural = '发布后端'

    name = models.CharField(max_length=50, verbose_name='项目名称', help_text='项目名称')
    server_flag = models.IntegerField(default=1, choices=((1, '测试'), (2, '生产')), verbose_name="服务器")
    user_flag = models.IntegerField(default=1, choices=((1, 'pyer'), (2, 'root')), verbose_name='服务器用户', help_text='服务器用户')
    server_ip = models.CharField(max_length=50, verbose_name='服务器IP', help_text='服务器IP')
    git_url = models.CharField(max_length=500, verbose_name='git地址', help_text='git地址')
    git_branch = models.CharField(max_length=500, verbose_name='git分支', help_text='master/develop')
    code_path = models.CharField(max_length=500, help_text='发布目标代码路径上一级', verbose_name='发布目标代码路径上一级')
    tmp_code_path = models.CharField(max_length=500, help_text='检测代码路径', verbose_name='检测代码路径')
    before_cmd = models.TextField(blank=True, null=True, help_text='部署前命令', verbose_name='部署前命令')
    after_cmd = models.TextField(blank=True, null=True, verbose_name='部署后命令', help_text='部署后命令')
    memo = models.CharField(max_length=500, null=True, blank=True, help_text='备注', verbose_name='备注')
    by_user = models.ForeignKey(User, null=True, blank=True, help_text='添加人', verbose_name='添加人',
                                on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class FrontEnd(TimeStampedModel):
    """
    配置表
    """

    class Meta:
        verbose_name = verbose_name_plural = '发布前端'

    name = models.CharField(max_length=50, verbose_name='项目名称', help_text='项目名称')
    server_flag = models.IntegerField(default=1, choices=((1, '测试'), (2, '生产')), verbose_name="服务器")
    user_flag = models.IntegerField(default=1, choices=((1, 'pyer'), (2, 'root')), verbose_name='服务器用户', help_text='服务器用户')
    server_ip = models.CharField(max_length=50, verbose_name='服务器IP', help_text='服务器IP')
    git_url = models.CharField(max_length=500, verbose_name='git地址', help_text='git地址')
    git_branch = models.CharField(max_length=500, verbose_name='git分支', help_text='master/develop')
    code_path = models.CharField(max_length=500, help_text='发布目标代码路径上一级', verbose_name='发布目标代码路径上一级')
    tmp_code_path = models.CharField(max_length=500, help_text='本地打包代码路径', verbose_name='本地打包代码路径')
    before_cmd = models.TextField(blank=True, null=True, help_text='打包代码前命令', verbose_name='打包代码前命令')
    after_cmd = models.TextField(blank=True, null=True, verbose_name='部署后命令', help_text='部署后命令')
    memo = models.CharField(max_length=500, null=True, blank=True, help_text='备注', verbose_name='备注')
    by_user = models.ForeignKey(User, null=True, blank=True, help_text='添加人', verbose_name='添加人',
                                on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class DeployLog(TimeStampedModel):
    """
    配置表
    """

    class Meta:
        verbose_name = verbose_name_plural = '发布日志'

    by_user = models.ForeignKey(User, null=True, blank=True, help_text='发布人', verbose_name='发布人',
                                on_delete=models.DO_NOTHING)
    project_flag = models.IntegerField(choices=((1, '后端'), (2, '前端')), default=1, verbose_name='项目分类', help_text='项目分类')
    content = models.TextField(blank=True, null=True, help_text='日志内容', verbose_name='日志内容')
    status = models.IntegerField(choices=((1, '成功'), (0, '失败')), default=0, verbose_name='状态', help_text='状态')
