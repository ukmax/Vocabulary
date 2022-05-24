"""vocabulary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import dictionaryapp.views as dictionaryapp

urlpatterns = [
    path('myauth/', include('myauth.urls', namespace='myauth')),

    path('admin/', admin.site.urls),
    path('topwords/', dictionaryapp.topwords, name='topwords'),
    path('checkwords/', dictionaryapp.checkwords, name='checkwords'),
    path('about/', dictionaryapp.about, name='about'),
    # path('', dictionaryapp.index, name='main'),
    path('', dictionaryapp.WordListView.as_view(), name='main'),
    # path('word/detail/<int:pk>/', dictionaryapp.word_detail, name='word_detail'),
    path('word/detail/<int:pk>/', dictionaryapp.WordDetailView.as_view(), name='word_detail'),
    path('word/create/', dictionaryapp.WordCreateView.as_view(), name='word_create'),
    path('word/update/<int:pk>/', dictionaryapp.WordUpdateView.as_view(), name='word_update'),

]
