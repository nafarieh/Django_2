from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
	path('', views.Home.as_view(), name='home'), #endpoint
	# path('<str:name>/', views.Home.as_view(), name='home'), #endpoint
	# path('', views.home, name='home'),
]