from django.urls import path
from . import views

urlpatterns = [
  path('hello/', views.say_hello),
  path('world/', views.my_world )
]
