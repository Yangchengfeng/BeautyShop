# 整理项目结构

1、添加名为 `apps` 的package，用于存放应用

    (1)users：用户信息(用户信息、短信验证码处理)
    (2)goods：商品信息(商品、类目、详情、轮播图)
    (3)trade：交易信息

2、添加名为 `extra_apps` 的的package，用于存放第三方包

3、添加名为 `templates` 的文件夹，用于存放静态文件

4、添加名为 `media` 的文件夹，用于存放资源，例如：图片

5、添加名为 `db_tools` 的文件夹，用于存放脚本文件

==> TODO：每次更新models，别忘了：
==>   - python manage.py makemigrations XXX
==>   - 使用：python manage.py migrate 生成数据表，可以通N过avicat Premium等工具看到        生成的表

==> TODO：这里起初使用django版本：1.11.9，出现了点击“增加商品”等“增加”操作时报错，解决方案：降低Django版本(最终使用1.11.7可以使用)

# 使用到的框架

【一】rest framework使用：Requirements & Installation（http://www.django-rest-framework.org/）

1、http://www.django-rest-framework.org/tutorial/3-class-based-views/

2、使用过滤功能时，使用`django-filter`和`django-rest-framework`两种：http://www.django-rest-framework.org/api-guide/filtering/#setting-filter-backends

https://django-filter.readthedocs.io/en/master/

① 搜索范围：^ 、= 、@、$

===> TODO：端口被占用时，使用` sudo lsof -t -i tcp:8000 | xargs kill -9`

【二】JWT :

【三】Django信号量：https://docs.djangoproject.com/en/1.11/ref/signals/

【四】social django：https://github.com/python-social-auth/social-app-django 

==> 相关配置：http://python-social-auth.readthedocs.io/en/latest/configuration/django.html