from django.urls import path
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns = [
    path('cpf/', include('cpf.urls')),
    path('admin/', admin.site.urls),
]
