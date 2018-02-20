# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = '用户管理'

    def ready(self):
        import users.signals