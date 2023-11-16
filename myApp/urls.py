from django.urls import path
from .import views
from .views import myApp

urlpatterns = [
   path('',views.myApp,name="myApp"),
]
