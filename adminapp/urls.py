import adminapp.views as adminapp
from django.urls import path

app_name = 'adminapp'
urlpatterns = [
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/read/', adminapp.UsersListView.as_view(), name='user_read'),
    path('users/update/<pk>/', adminapp.UsersUpdateView.as_view(), name='user_update'),
    path('users/delete/<pk>/', adminapp.user_delete, name='user_delete'),

    path('categories/create/', adminapp.CategoryCreateView.as_view(), name='category_create'),
    path('categories/read/', adminapp.categories_read, name='category_read'),
    path('categories/update/<pk>/', adminapp.category_update, name='category_update'),
    path('categories/delete/<pk>/', adminapp.category_delete, name='category_delete'),
    path('categories/products/read/<pk>/', adminapp.CategoryDetailView.as_view(), name='products_read'),

    path('products/create/category/<pk>/', adminapp.product_create, name='product_create'),

    path('products/update/<pk>/', adminapp.product_update, name='product_update'),
    path('products/delete/<pk>/', adminapp.ProductDeleteView.as_view(), name='product_delete'),
    path('products/detail/<pk>/', adminapp.ProductDetailView.as_view(), name='product_detail'),
]
