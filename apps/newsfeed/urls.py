from django.urls import path, include

from . import views

app_name = "newsfeed"
urlpatterns = [
    path(
        "newsfeed/",
        views.NewsfeedView.as_view(template_name="newsfeed/landing.html"),
        name="landing",
    ),
]
