from audioop import reverse

from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, RedirectView


class SignUpView(CreateView):
    model = User


class SignInView(LoginView):
    pass


class LogoutView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('home')
