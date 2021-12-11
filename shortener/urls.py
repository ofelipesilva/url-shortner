from django.urls import path

from . import views

app_name = 'shortner'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create_short'),
    path('<str:uuid>', views.shortened_go, name='shortened_go'),
]
