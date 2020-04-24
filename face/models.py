from django.db import models
from django.urls import reverse
from django.shortcuts import redirect

class Post(models.Model):
	title   = models.CharField(max_length = 100)
	author  = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	content = models.TextField()
	picture = models.ImageField()

	def __str__(self):
		return self.title 

	def get_absolute_url(self, *args, **kwargs):
		return reverse('content')

