from django.urls import path
from . import views

urlpatterns = [
    path('', views.create, name='links'),
    path('<str:url>', views.redirect_link, name='redirect'),
]
