from django.urls import path
from apps.user.views import UserAPI


urlpatterns = [
    path('users', UserAPI.as_view()),
]