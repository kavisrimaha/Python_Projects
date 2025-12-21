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

]
