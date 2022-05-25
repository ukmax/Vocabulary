from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from myauth.forms import MyUserCreateForm
from myauth.models import MyUser


class MyUserCreateView(CreateView):
    model = MyUser
    success_url = '/'
    form_class = MyUserCreateForm