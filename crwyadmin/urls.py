#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wuyue92tree@163.com
from django.conf.urls import url, include
from crwyadmin.sites import crwy_site
from crwyadmin.views import *

urlpatterns = [
    url(r'^', crwy_site.urls),
    url(r'^index1/', Index1View.as_view(), name='index1'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^select_language/', SelectLanguageView.as_view(), name='select_language'),
    url(r'^config/(?P<slug>.*)/', ConfigView.as_view(), name='config'),

    # 用于进行语言切换
    url(r'^i18n/', include('django.conf.urls.i18n'), name='i18n'),
]
