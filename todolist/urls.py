from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete/<int:task_id>/', views.delete_element, name='delete_element'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('pending/<int:task_id>/', views.pending_task, name='pending_task'),
    path('contactus/', views.contactus, name='contactus'),
    path('activity/', views.activity, name='activity'),
]
