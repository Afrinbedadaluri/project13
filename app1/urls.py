from django.urls import path
from app1.views import *
app_name='one'
urlpatterns=[
    path('animals/',animals,name='animals'),
    path('birds/',birds,name='birds'),
]