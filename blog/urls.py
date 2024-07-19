from django.urls import path
from .views import index, IndexView
from .views import BlogListView, BlogCreateView, create_done, BlogDetailView
from .views import BlogDeleteView, delete_done, CategoryView, SearchPostView


app_name = 'blog'
urlpatterns = [
    path('index', index, name="index"),
    path('index_class', IndexView.as_view(), name="index_class"),
    path('', BlogListView.as_view(), name="blog_list"),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('create_done/', create_done, name='create_done'),     path('detail/<int:pk>/', BlogDetailView.as_view(), name="detail"),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('delete_done/', delete_done, name='delete_done'),
    path('category/<str:category>/', CategoryView.as_view(), name='category'),
    path('search_list/', SearchPostView.as_view(), name='search_list'),
]
