from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name='index'),
    path('employees',views.Fun_Data,name='Fun_Data'),
]