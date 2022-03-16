from django.urls import path
from .views import  todo_detail, todoCreate,home


urlpatterns = [
  path('',home),
  #path('todolist/',todoList),
  path('todocreate/',todoCreate),
  #path('todos/',todoListCreate),
  path('todos/<int:pk>',todo_detail),
  #path('todoupdate/<int:pk>',todo_update),
  #path('tododelete/<int:pk>',todo_delete),
  
]
