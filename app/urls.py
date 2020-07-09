
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.RegistrationPage,name="registerpage"),
    path("registeruser/",views.RegisterUser,name="registeruser"),
    path("loginpage/",views.LoginPage,name="loginpage"),
    path("loginuser/",views.LoginUser,name="loginuser"),
    path("imagepage/",views.ImagePage,name="imagepage"),
    path("upload/",views.ImageUpload,name="upload"),
    path("fetchdata/",views.FetchFile,name="fetch"),
    path("jspage/",views.JsPage,name="jspage"),
]
