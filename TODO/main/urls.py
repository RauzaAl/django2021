from django.urls import path, re_path
from main.views import todo_list, todo_list_complited\

urlpatterns = [
    path('', todo_list),
    path('todos/', todo_list),
    path('todos/1/complited/', todo_list_complited),
]