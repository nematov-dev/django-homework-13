from django.urls import path

from products import views


app_name = 'products'

urlpatterns = [
    path('',views.ProductListView.as_view(),name='product'),
    path('product/<int:pk>/',views.ProductDetailView.as_view(),name='detail'),
]