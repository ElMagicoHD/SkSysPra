from django.urls import path

from . import views

urlpatterns = [
    path('', views.overview, name='overview'),
    path('new/', views.newTodo, name='new-todo'),
    path('edit/', views.edit, name='edit-todo'),
    path('addTodo/', views.addTodo, name='add-todo'),
    path('deleteTodo/<int:todo_id>/', views.deleteTodo, name='delete-todo')
]