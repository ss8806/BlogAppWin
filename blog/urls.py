from django.urls import path
from .views import index, IndexView
from .views import BlogListView


app_name = 'blog'
urlpatterns = [
    path('index', index, name="index"),
    path('index_class', IndexView.as_view(), name="index_class"),
    path('', BlogListView.as_view(), name="blog_list"),
]
