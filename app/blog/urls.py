from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomepageView.as_view(), name="homepage"),
    path("<slug:post>", views.post_single, name="post_single"),
]
