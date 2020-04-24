from django.urls import path, include
from .views import ContentView, BlogDetailView, BlogContentCreateView, BlogContentUpdateView, BlogContentDeleteView

urlpatterns = [
	path('', ContentView.as_view(), name='content'),
	path('blog-post/new/', BlogContentCreateView.as_view(), name= 'new-post'),
	path('blog-post/<int:pk>/', BlogDetailView.as_view(), name= 'post-detail'),
	path('blog-post/<int:pk>/edit/', BlogContentUpdateView.as_view(), name= 'edit-post'),
	path('blog-post/<int:pk>/delete/', BlogContentDeleteView.as_view(), name= 'delete-post')
]