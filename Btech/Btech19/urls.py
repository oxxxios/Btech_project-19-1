from django.urls import path
import views

urlpatterns = [
  path('login/', views.LoginAPIView.as_view()),
  path('register/', views.RegisterAPIView.as_view()),

]
