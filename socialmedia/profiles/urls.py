from django.urls import path
from .views import  my_profileview

app_name = 'profiles'

urlpatterns = [
    path('myprofile/', my_profileview, name=my_profileview)
]
