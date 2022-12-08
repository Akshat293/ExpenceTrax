from django.shortcuts import render
from django.views import View
# Create your views here.


class RegisterationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html', {})

class LoginView(View):
    pass

class LogoutView(View):
    pass

class PasswordResetView(View):
    pass

