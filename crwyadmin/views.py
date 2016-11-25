# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
from django.views.generic import *
from django.contrib.auth.models import User
from .forms import RegisterForm
from .sites import admin_site
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
            user.is_staff = True
            user.save()
            return HttpResponse("注册成功")
        else:
            return render(request, self.template_name, locals())

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        context['site_title'] = admin_site.site_title
        context['site_header'] = admin_site.site_header
        return context
