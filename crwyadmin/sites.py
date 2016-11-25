#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wuyue92tree@163.com

from django.contrib.admin.sites import AdminSite
from django.utils.translation import ugettext_lazy


class MyAdminSite(AdminSite):
    site_header = ugettext_lazy("Crwy Administration")
    site_title = ugettext_lazy("Crwy site admin")

admin_site = MyAdminSite(name='crwyadmin')
