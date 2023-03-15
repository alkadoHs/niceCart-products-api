from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('product-list/', views.productList, name='task-list'),
    path('product-detail/<str:pk>/', views.productDetails, name='task-detail'),
    path('product-create/', views.productCreate, name="task-create"),
    path('product-update/<str:pk>/', views.productUpdate, name='task-update'),
    path('product-delete/<str:pk>/', views.productDelete, name='task-delete'),
]
