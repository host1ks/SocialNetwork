from django.urls import path
from .views import RegistrationAPIView, LoginAPIView

app_name = 'users'
urlpatterns = [
    path('register/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]
