from django.urls import path

from .views import UserAPIView

urlpatterns = [
    path('fetch', UserAPIView.as_view(), name='user')
]