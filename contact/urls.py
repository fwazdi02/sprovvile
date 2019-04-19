from django.urls import path
from .views import add_contact

urlpatterns = [
    path('add', add_contact, name='add')
]