from django.urls import path, re_path
from main.views import todo_list, todo_list_completed\

urlpatterns = [
    path('', todo_list),
    path('todos/<int:id>/', todo_list),
    path('todos/<int:id>/completed/', todo_list_completed),
]