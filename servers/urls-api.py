from django.urls import path
from . import views
urlpatterns = [
    path('servers/', views.server_list, name='api_server_list'),
    path('servers/<int:pk>/', views.server_detail_api, name='api_server_detail'),
    path('servers/create/', views.server_create_api, name='api_server_create'),
]