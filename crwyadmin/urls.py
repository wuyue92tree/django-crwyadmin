#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wuyue92tree@163.com
from django.conf.urls import url, include
from .sites import admin_site
from .views import *

urlpatterns = [
    url(r'^', admin_site.urls),
    url(r'^index1/', Index1View.as_view(), name='index1'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^select_language/', SelectLanguageView.as_view(), name='select_language'),
    url(r'^i18n/', include('django.conf.urls.i18n'), name='i18n'),
]