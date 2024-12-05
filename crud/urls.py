from django.urls import path
from . import views, admin

urlpatterns = [
    path("", views.index, name="index"),
    path("createemployee", views.createuser, name="createuser"),
    path("deleteemployee", views.deleteuser, name="deleteuser"),
    path("viewemployees", views.viewusers, name="viewusers"),
    path("updateemployee", views.viewusers, name="updateuser"),
]