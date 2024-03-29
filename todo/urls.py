"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.conf.urls import url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from todo.views import ToDoListView, ToDoDetailView
from django.urls import include, path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^todo/$', TemplateView.as_view(template_name='todo/index.html')),
    url(r'^todo/api/$', ToDoListView.as_view()),
    url(r'^todo/api/(?P<pk>[0-9]+)/', ToDoDetailView.as_view())
]
