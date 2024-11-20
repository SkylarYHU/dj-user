from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, profile_view, user_list_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name="profile"),
    path('users/', user_list_view, name='user_list'),
]
