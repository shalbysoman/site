from django.urls import path

from . import views

urlpatterns = [
    path('showProducts', views.ShowAllProducts, name='showProducts'),
    path('product/<int:pk>/', views.productDetail, name='product'),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('updateProduct/<int:pk>/', views.updateProduct, name='updateProduct'),
    path('deleteProduct/<int:pk>/', views.deleteProduct, name='deleteProduct'),
    path('search/', views.searchBar, name='search'),
    path('product/<int:pk>/add-comment', views.add_comment, name='add-comment'),
    path('product/<int:pk>/delete-comment', views.delete_comment, name='delete-comment'),
    path('admin_show', views.admin_Show, name='admin_show'),
    path('adminproduct/<int:pk>/', views.admin_product, name='adminproduct'),



]