from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('infos/', views.get_info_list, name='info-list'),
    path('infos/create/', views.create_info, name='info-create'),
]
