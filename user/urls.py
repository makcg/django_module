from django.urls import path
from .views import SignUpView, SignInView, LogoutView

app_name = 'user'
urlpatterns = [
    path("sign-up/", SignUpView.as_view(), name="sign-up"),
    path("sign-in/", SignInView.as_view(), name="sign-in"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
