# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
from django.views.generic import *
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy
from crwyadmin.forms import RegisterForm, CrwyConfigForm
from crwyadmin.models import CrwyadminConfig
from crwyadmin.sites import crwy_site

# Create your views here.


class Index1View(TemplateView):
    template_name = 'crwyadmin/index1.html'


class SelectLanguageView(TemplateView):
    template_name = 'crwyadmin/select_language.html'


class RegisterView(TemplateView):
    template_name = 'crwyadmin/register.html'

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.data['username'], email=form.data['email'], password=form.data['password'])
            user.is_active = True
            user.save()
            return HttpResponse("注册成功")
        else:
            return render(request, self.template_name, locals())

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        context['site_title'] = crwy_site.site_title
        context['site_header'] = crwy_site.site_header
        return context


class ConfigView(UpdateView):
    template_name = 'crwyadmin/config.html'
    model = CrwyadminConfig
    form_class = CrwyConfigForm
    slug_field = 'slug'
    success_url = '/crwyadmin/config/system/'

    def get_context_data(self, **kwargs):
        context = super(ConfigView, self).get_context_data(**kwargs)
        context['title'] = _("System_Config")
        return context

