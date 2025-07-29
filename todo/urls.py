from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
]