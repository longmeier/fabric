from django.db import models
# 参考：https://docs.djangoproject.com/en/1.10/topics/auth/customizing/#a-full-example

from django.contrib.auth.models import AbstractUser, UserManager, Group, GroupManager, User as U


# Create your models here.

class MyUserManager(UserManager):
    def get_queryset(self):
        # 取用户信息的时候，同时把用户的配置文件读取出来。避免出现多条SQL访问
        return super(MyUserManager, self).get_queryset()


class User(AbstractUser):
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username', 'password']

    objects = MyUserManager()
    pass