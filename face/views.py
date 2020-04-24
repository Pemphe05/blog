from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy



class ContentView(ListView):
	model = Post
	template_name = 'face/content.html'
	context_object_name = 'blogs'

	# template_name = 'face/content.html'
	# context_object_name = 'blogs'

	# def get_queryset(self):
	# 	return Post.objects.all()

class BlogDetailView(DetailView):
	model = Post
	template_name = 'face/post_detail.html'
	context_object_name = 'posts'

class BlogContentCreateView(CreateView):
	model = Post
	template_name = 'face/new_post.html'
	fields = ['title', 'author', 'content','picture']
	# fields = ['title', 'author', 'content']
	

class BlogContentUpdateView(UpdateView):
	model = Post
	template_name = 'face/edit_post.html'
	fields = ['title', 'content']


	def form_valid(self, form):
		form.instance.author=self.request.user
		return super().form_valid(form)

	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
		return False 

class BlogContentDeleteView(DeleteView):
	model = Post
	template_name = 'face/delete_post.html'
	context_object_name = 'deletes'
	success_url = reverse_lazy('content')

	