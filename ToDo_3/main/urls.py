from django.urls import path, re_path
from main.views import TodoListViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('todos', TodoListViewSet, basename='todo')

urlpatterns = router.urls

# urlpatterns = [
#     path('', todo_list),
#     path('todos/<int:id>/', todo_list),
#     path('todos/<int:id>/completed/', todo_list_completed),
# ]