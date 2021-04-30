from django.urls import path
from .views import PostView, LikeView, DetailLikeView

app_name = 'main'
urlpatterns = [
    path('post', PostView.as_view()),
    path('like', LikeView.as_view()),
    path('analytics/', DetailLikeView.as_view()),
]
