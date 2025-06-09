from django.urls import path
from . import api

urlpatterns = [
    path('', api.get_jobs, name='get_jobs'),
    path('create/', api.create_job, name='create_job'),
    path('delete/<uuid:id>/', api.delete_job, name='delete_job'),
]