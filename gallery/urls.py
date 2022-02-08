from django.urls import path
from gallery import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('gallery/', views.gallery, name = 'gallery'),
    path('photo/<str:pk>/', views.viewphoto, name = 'viewphoto'),
    path('add/', views.addphoto, name = 'add'),
    path('delete-product/<str:pk>', views.deleteImage, name="delete-image"),

    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
]