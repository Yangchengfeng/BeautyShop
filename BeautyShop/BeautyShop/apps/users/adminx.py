# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from .models import VerifyCode

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = "完美女孩后台"
    site_footer = "beautyshop"

class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "add_time"]

xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)