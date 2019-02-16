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
        verbose_name = verbose_name_plural = '配置表'

    name = models.CharField(max_length=50, verbose_name='服务器名称', help_text='服务器名称')
    flag = models.IntegerField(default=1, choices=((1, '测试'), (2, '生产')), verbose_name="服务器")
    user_flag = models.IntegerField(default=1, choices=((1, 'pyer'), (2, 'root')), verbose_name='服务器用户', help_text='服务器用户')
    ip = models.CharField(max_length=50, verbose_name='IP', help_text='IP')
    code_path = models.CharField(max_length=500, help_text='更新到代码路径上一级', verbose_name='更新到代码路径上一级')
    before_cmd = models.TextField(blank=True, null=True, help_text='部署前命令', verbose_name='部署前命令')
    after_cmd = models.TextField(blank=True, null=True, verbose_name='部署后命令', help_text='部署后命令')
    git_url = models.CharField(max_length=500, verbose_name='git地址', help_text='git地址')
    tmp_code_path = models.CharField(max_length=500, help_text='tmp代码路径', verbose_name='tmp代码路径')
    status = models.IntegerField(choices=((1, '正常'), (0, '不可用')), default=0, verbose_name='配置状态', help_text='配置状态')
    memo = models.TextField(null=True, blank=True, help_text='注意事项', verbose_name='注意事项')
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
    content = models.TextField(blank=True, null=True, help_text='日志内容', verbose_name='日志内容')
    status = models.IntegerField(choices=((1, '成功'), (0, '失败')), default=0, verbose_name='状态', help_text='状态')
