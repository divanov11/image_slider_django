from . import views
from django.urls import path

urlpatterns = [
	path('', views.slider, name="slider"),
]