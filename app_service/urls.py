from django.urls import path
from app_service.views import *

urlpatterns = [
    path('', MainView.as_view(), name='main'),
]
