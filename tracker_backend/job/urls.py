from django.urls import path
from . import api

urlpatterns = [
    path('create/', api.create_job, name='create_job'),
]