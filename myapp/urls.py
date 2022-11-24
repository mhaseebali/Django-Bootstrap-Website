from django.urls import path
from . import views

urlpatterns = [
    # path('', views.req),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logOutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('', views.req1),
    path('designs/', views.req2),
]