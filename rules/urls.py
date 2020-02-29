''' Django URLs '''
from django.urls import path
from rules import views


urlpatterns = [
    path('', views.main, name='main'),
    path('test_view/<int:rule_id>/', views.test_view, name='test_view'),
    path('filter_settings/<int:filter_id>/',
         views.filter_settings, name='filter_settings'),
    path('filter_settings/<int:filter_id>/attr_creation/',
         views.attr_creation, name='attr_creation'),
    path('attr_settings/<int:attr_id>/',
         views.attr_settings, name='attr_settings')
]
