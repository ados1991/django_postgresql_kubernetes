from django.urls import path, re_path
from . import views

urlpatterns = [
    path('posts', views.get_post_posts.as_view()),
    re_path(r'^posts/(?P<id>[0-9]+)$', views.get_delete_update_post.as_view()),
]