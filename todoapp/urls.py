# from django.urls import path
# from django.contrib.auth import views as auth_views
# from . import views
# from django.contrib import admin

# urlpatterns = [
#     path('', views.user_login, name='login'),      # login page
#     path('task_list/', views.task_list, name='task_list'),  # protected page
#     path('logout/', views.user_logout, name='logout'),      # optional logout
#     path('signup/', views.signup, name='signup'), #signup
#      path('task/create/', views.task_create, name='task_create'),
# ]

from django.urls import path
from . import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),

    path('task_list/', views.task_list, name='task_list'),
    path('task/create/', views.task_create, name='task_create'),
path('task/update/<int:pk>/', views.task_update, name='task_update'),
    path('task/delete/<int:pk>/', views.task_delete, name='task_delete'),

    # Routines
    path('routines/', views.routine_list, name='routine_list'),
    path('routine/create/', views.routine_create, name='routine_create'),
    path('routine/delete/<int:pk>/', views.routine_delete, name='routine_delete'),
    path('routine/toggle/<int:pk>/', views.routine_toggle, name='routine_toggle'),

    # Notes
    path('notes/', views.note_list, name='note_list'),
    path('note/create/', views.note_create, name='note_create'),
    path('note/update/<int:pk>/', views.note_update, name='note_update'),
    path('note/delete/<int:pk>/', views.note_delete, name='note_delete'),
]
