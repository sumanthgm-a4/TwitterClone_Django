from django.urls import path
from app1 import views

urlpatterns = [
    path("", views.render_home, name="home"),
    path("login", views.render_login, name="login"),
    path("profile", views.render_profile, name="profile"),
    path("logout", views.render_logout, name="logout"),
    path("register", views.render_register, name="register"),
    path("create", views.render_create_post, name="create"),
    path("delete/<str:post_id>", views.render_delete, name="delete"),
    path("display/<str:post_id>", views.render_display, name="display"),
]