#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wuyue92tree@163.com

from django.contrib.admin.sites import AdminSite
from django.utils.translation import ugettext_lazy as _


class MyAdminSite(AdminSite):
    site_header = _("Crwy Administration")
    site_title = _("Crwy site admin")

crwy_site = MyAdminSite(name='crwyadmin')
