from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_view, name='list_view'),
     path('tasks/', views.get_tasks, name='get_tasks'),    # API endpoint to fetch tasks
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/delete/<int:id>/', views.delete_task, name='delete_task'),
    path('tasks/delete/all/', views.delete_all_tasks, name='delete_all_tasks'),  # New path
]
