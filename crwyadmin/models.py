# -*- coding: utf-8 -*-
# author: wuyue92tree@163.com
#
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class CrwyadminConfig(models.Model):
    slug = models.CharField(max_length=100)
    is_register = models.BooleanField(default=False, verbose_name=_('Is_Register_Open'))
    is_forgetpasswd = models.BooleanField(default=False, verbose_name=_('Is_Forgetpasswd_Open'))
    manager_email = models.CharField(max_length=100, verbose_name='Manager_Email')
    version = models.CharField(max_length=100, verbose_name='CrwyAdmin_Version')

    class Meta:
        db_table = 'crwyadmin_config'
