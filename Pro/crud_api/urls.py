from django.urls import path
from .views import *

urlpatterns = [
    path('',studentList),
    path('details/<int:id>/',studentDetails)
]