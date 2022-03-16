from django.urls import path
from .views import todoCreate, todoList,home, todoListCreate


urlpatterns = [
  path('',home),
  path('todolist/',todoList),
  path('todocreate/',todoCreate),
  path('todos/',todoListCreate)
  
]
