from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rough/', views.rough, name='rough'),
    path('admindash/', views.admindash, name='admindash'),
    path('add_dress/', views.add_dress, name='add_dress'),
    path('admin_index/', views.admin_index, name='admin_index'),
    path('view_dress/', views.view_dress, name='view_dress'),
    path('delete_dress/<int:dress_id>/', views.delete_dress, name='delete_dress'),
    path('collections/<str:gender>/', views.collections, name='collections'),
    path('filter_list/<str:gender>/', views.filter_list, name='filter_list'),
    path('add_to_wishlist/<int:dress_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('detail/<int:dress_id>/', views.detail, name='detail'),

    path('admin_login/', views.admin_login, name='admin_login'),


]
