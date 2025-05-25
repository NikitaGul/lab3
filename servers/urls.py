from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.default_app_page),
    path('', views.server_list, name='server_list'),
    path('<int:server_id>/', views.server_detail, name='server_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='servers/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('secure/', views.secure_page, name='secure'),
]