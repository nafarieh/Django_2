from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
	path('register/', views.UserRegister.as_view()), #endpoint

]