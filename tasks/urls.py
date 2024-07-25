from django.urls import path
from . import views

urlpatterns = [
    path("", views.addtask, name="tasks"),
    path("update/<int:pk>", views.updatetask, name="update"),
    path("delete/<int:pk>", views.deletetask, name="delete"),
]
