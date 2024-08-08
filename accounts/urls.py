from django.urls import path
from . import views

urlpatterns = [
    # path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout')
    path('', views.login_user, name='login'),

    path('register/', views.register_user, name='register'),
    path('home/', views.home_page, name='home'),
    path('logout/', views.log_out, name='logout'),
    path('index/', views.index_detail, name='index'),
    path('list/', views.list_user, name='list'),
    path('details/<int:user_id>/', views.detail_user, name='details'),
    path('updateuser/<int:user_id>/', views.update_user, name='updateuser'),
    path('adminhome/', views.admin_home, name='adminhome'),

]