from django.urls import path
from .views import UserProfileView


urlpatterns = [
    path("registre/", UserProfileView.as_view(), name="UserProfile")
]
