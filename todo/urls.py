from django.urls import path
from .views.todo_view import TodoListView, TodoCreateView, TodoDeleteView, change_status

urlpatterns = [
    path('', TodoListView.as_view(), name="home-page"),
    path('add', TodoCreateView.as_view(), name="add-todo"),
    path('delete/<int:pk>', TodoDeleteView.as_view(), name="delete-todo"),
    path('change-status/<int:id>/<str:status>',
         change_status, name="change-status"),
]
