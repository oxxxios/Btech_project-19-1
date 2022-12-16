from django.contrib import admin
from django.urls import path, include
from django.urls import path
from Btech19 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', views.ProductListAPIView.as_view()),
    path('api/v1/products/<int:id>/', views.ProductUpdateDeleteAPIView.as_view()),
    # path('api/v1/products/search/, ')
        ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls'))
    ]


