from django.urls import path

from . import views

urlpatterns = [
    path("blog", views.blog, name="blog"),
    path("podcasts", views.podcasts, name="podcasts")
]