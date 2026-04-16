from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('painel/', views.PainelView.as_view(), name='painel'),
    path('perfil/', views.PerfilView.as_view(), name='perfil'),
]
