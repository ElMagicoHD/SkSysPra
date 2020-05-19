from django.urls import path

from . import views

urlpatterns = [
    path('', views.overview, name='overview'),
    path('new', views.newTodo, name='new-todo'),
    path('edit', views.edit, name='edit-todo')
]