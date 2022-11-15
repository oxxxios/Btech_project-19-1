from django.urls import path
from users.views import *

urlpatterns = [
  path('login/', login_),
  path('register/', register_),

]