from django.urls import path
import website.views as views

urlpatterns = [
    path("",views.home,name="home"),
    path("login/",views.login_user,name="login"),
    path("logout/",views.logout_user,name="logout")

]