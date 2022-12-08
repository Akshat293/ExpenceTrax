from django.urls import path

from .views import RegisterationView, LoginView, LogoutView, PasswordResetView

urlpatterns = [

    path('register/', RegisterationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
]