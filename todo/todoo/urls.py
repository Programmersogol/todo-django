from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup_view, name='signup'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('todoo', views.todo_view, name='todo'),
    path('edit_todo/<int:srno>/', views.edit_todo_view, name='edit_todo'),
    path('delete_todo/<int:srno>/', views.delete_todo_view, name='delete_todo'),
    path('edit_todo_ajax/<int:srno>/', views.edit_todo_ajax, name='edit_todo_ajax'),
    path('delete_todo_ajax/<int:srno>/', views.delete_todo_ajax, name='delete_todo_ajax'),
    path('toggle_done/<int:srno>/', views.toggle_done, name='toggle_done'),



]
