from django.urls import path, include
from . import views
from django.contrib.auth import views as view

urlpatterns = [
    # path('', views.default_app_page),
    path('', views.server_list, name='server_list'),
    path('<int:server_id>/', views.server_detail, name='server_detail'),
    path('login/', view.LoginView.as_view(template_name='servers/login.html'), name='login'),
    path('logout/', view.LogoutView.as_view(next_page='login'), name='logout'),
    path('secure/', views.secure_page, name='secure'),
    path('api/', include('servers.urls-api')),
    path('csv/', views.csv_view, name='csv_view'),
    path('csv/delete/', views.csv_delete, name='csv_delete'),
    path('servers/delete/<int:server_id>/', views.delete_server, name='delete_server'),
]