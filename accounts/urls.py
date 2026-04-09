from django.urls import path
from .views import RegisterView, login

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', login),
]