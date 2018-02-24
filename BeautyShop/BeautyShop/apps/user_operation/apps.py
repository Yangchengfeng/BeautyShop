# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class UserOperationConfig(AppConfig):
    name = 'user_operation'
    verbose_name = '用户操作管理'

    def ready(self):
        import user_operation.signals