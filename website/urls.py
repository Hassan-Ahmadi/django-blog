from django.urls import path

from .views import about_view, contact_us_view, index_view

app_name = "website"


urlpatterns = [
    path("about", about_view, name="about"),
    path("contact", contact_us_view, name="contact"),
    path("", index_view, name="index"),
    ]
