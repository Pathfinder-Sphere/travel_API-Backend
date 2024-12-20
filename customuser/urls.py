from django.urls import path
from .import views

urlpatterns = [
    path('', views.Signup.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout')
]