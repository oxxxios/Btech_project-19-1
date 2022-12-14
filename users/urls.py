from .views import SignUpView, LoginView
from django.urls import path
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns=[
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('jwt/create', TokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh', TokenRefreshView.as_view(), name='token-refresh'),
    path('jwt/verify', TokenVerifyView.as_view(), name='token-verify')
]