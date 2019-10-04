from django.urls import path
import apps.sm_shop.views as views

urlpatterns = [
    path('', views.index),
    path('check_user/', views.check_user)
]
