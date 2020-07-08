from django.urls import path

from . import views


urlpatterns = [
    path('', views.products_list, name='products-list'),
    path('<slug:category_slug>/', views.products_list, name='product-category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product-detail')
]