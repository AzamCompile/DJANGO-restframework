from django.urls import path
from product.views import ProductCreateAPIView, ProductUpdateAPIView, ProductDeleteAPIView, ProductRetrivAPIView

urlpatterns = [
    path('',ProductCreateAPIView.as_view()),
    path('update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='product-delete'),
    path('ditile/<int:pk>/', ProductRetrivAPIView.as_view(), name='product-delete'),

]