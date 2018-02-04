# Databases处理

1、修改DATABASES设置

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'beautyshop',
        'USER': 'root',
        'PASSWORD': 'aaaaa',
        'OPTIONS':{'init_command': 'SET default_storage_engine=INNODB;',}
    }
}
```

2、使用Navicat premium创建数据库（使用utf-8）
