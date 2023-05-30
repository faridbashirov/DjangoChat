from django.urls import path
from django.contrib.auth import views as auth_views 
from .views import home,signup,Logout
urlpatterns =[
    path("",home,name="home"),
    path("signup/",signup.as_view(),name="signup"),
    path("login/",auth_views.LoginView.as_view(template_name="login.html"),name="login"),
    path("logout/",Logout,name="logout"),
    


]