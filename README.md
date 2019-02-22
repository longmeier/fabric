# fabric

#### 介绍
该项目可用于定制化小型公司的代码部署。
开发环境是用django2 + Fabirc3 + python3开发的。
部署用centos7 + gunicorn + nginx + mysql5.7

#### 软件架构
软件架构说明
src/config django一些配置包括数据库、日志、url、静态文件配置
src/templates 页面模板
src/tools  数据库models字段的定义、执行命令具体看admin.py 里面的代码。
由于python在执行发布命令中有的命令耗时比较长可以把延迟时间加大一点

#### 安装教程
默认python环境已经装好
1. 克隆代码
   git clone https://github.com/longmeier/fabric.git
2. 添加 配置私密文件 cd fabric & touch .env
3. .env文件要保存内容
    DATABASE_URL="mysql://root:1234@127.0.0.1/fabric"  
    TST_PYER_PWD="xxx"  ;测试服务器 pyer 密码
    TST_ROOT_PWD="xxx"  ;测试服务器 root 密码
    PRD_PYER_PWD="xxx"
    PRD_ROOT_PWD="xxx"
    
4. 同步数据库 创建用户
   python manage.py makemigrations & python manage.py migrate  
5. 安装环境
   pip install -r requirements.txt
6. 重启项目
   sudo supervisorctl restart fabric
7. gunicorn配置
    from __future__ import unicode_literals
    import multiprocessing
    
    bind = "127.0.0.1:9034"
    timeout = 60 * 30
    workers = multiprocessing.cpu_count()
    loglevel = "info"
    proc_name = "fabric"

#### 使用说明

1. 写的文档略有简洁，因为本身并不复杂，会django的话一般都能看的懂。
2. xxxx
3. xxxx

#### 参与贡献

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request


#### 码云特技

1. 使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2. 码云官方博客 [blog.gitee.com](https://blog.gitee.com)
3. 你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解码云上的优秀开源项目
4. [GVP](https://gitee.com/gvp) 全称是码云最有价值开源项目，是码云综合评定出的优秀开源项目
5. 码云官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6. 码云封面人物是一档用来展示码云会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)