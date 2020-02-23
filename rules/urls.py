from django.urls import path
from rules import views


urlpatterns = [
    path('', views.test),
]
