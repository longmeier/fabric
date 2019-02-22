# fabric

#### 介绍
代码部署 
开发环境是用django2 + Fabirc3 + python3开发的。
可用于定制化小型公司的代码部署。
部署用centos7 + gunicorn + nginx + mysql5.7

#### 软件架构
软件架构说明
tools-前端、后端模型，发布命令不一样，所以写了两个models
具体看admin.py 里面的命令。
由于python在执行发布命令中有的命令耗时比较长可以把延迟时间加大一点

#### 安装教程

1. git pull
2. python3 manage.py makemigrations
3. python3 manage.py migrate
2. pip install -r requirements.txt
3. sudo supervisorctl restart fabric

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