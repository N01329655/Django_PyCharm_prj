# my imports
from django.urls import path
from blog.views import (
        BlogDetailView,
        BlogCreateView,
        BlogListView,
        BlogUpdateView,
        BlogDeleteView,
)

urlpatterns = [
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('', BlogListView.as_view(), name='homepage'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail_page'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'),

]

