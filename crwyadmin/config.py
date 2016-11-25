#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wuyue92tree@163.com

import os

CRWYADMIN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from django.utils.translation import ugettext_lazy as _

LANGUAGES = (
    ('zh-hans', _('Simplified Chinese')),
    ('en', _('English')),
)

LOCALE_PATHS = (
    os.path.join(CRWYADMIN_DIR, "crwyadmin/locale"),
)


STATIC_ROOT = os.path.join(os.path.dirname(CRWYADMIN_DIR), 'static')
