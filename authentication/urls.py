from django.urls import path
from authentication import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='index'),
    path('login/',views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name="logout"),
]