from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('convert/', views.convert_form, name='guest_user_convert'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name ="home.html"), name='logout'),
]

