# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
from .models import Zeet, Comment
from .forms import ZeetPostForm, CommentForm

def all_zeets(request):
	zeets = Zeet.objects.filter(zeeter = request.user)
	return render(request, 'zeets/home.html', {'zeets':zeets})

@login_required
def post_zeet(request):
	if request.method == 'POST':
		form = ZeetPostForm(data = request.POST, files = request.FILES)
		if form.is_valid():
			new_zeet = form.save(commit = False)
			new_zeet.zeeter = request.user
			new_zeet.save()
			return redirect('zeets:feed')
	else:
		form = ZeetPostForm()
	return render(request, 'zeets/post.html', {'form':form})

@login_required
def edit_zeet(request, zeet_id):
	zeet = get_object_or_404(Zeet, pk = zeet_id)
	if request.method == 'POST':
		form = ZeetPostForm(data = request.POST, instance = zeet, files = request.FILES)
		if form.is_valid():
			form.save()
			return redirect('zeets:home')
	else:
		form = ZeetPostForm(instance = zeet)
	return render(request, 'zeets/post.html', {'zeet':zeet, 'form':form})

@login_required
def delete_zeet(request, zeet_id):
	zeet = get_object_or_404(Zeet, pk = zeet_id)
	zeet.delete()
	messages.info(request, 'Zeet was successfully deleted')
	return redirect('zeets:home')

@login_required
def comment(request, zeet_id):
	zeet = get_object_or_404(Zeet, pk = zeet_id)
	comments = zeet.comments.all()
	if request.method == 'POST':
		form = CommentForm(data = request.POST)
		if form.is_valid():
			new_comment = form.save(commit = False)
			new_comment.zeet = zeet 
			new_comment.user = request.user 
			new_comment.save()
			messages.success(request, 'comment added successfully')
	else:
		form = CommentForm()
	return render(request, 'zeets/comment.html', {'zeet':zeet, 'comments':comments, 'form':form})

@login_required
def delete_comment(request, comment_id):
	comment = get_object_or_404(Comment, pk = comment_id)
	comment.delete()
	messages.info(request, 'comment was deleted')
	return redirect('zeets:home')

@login_required
def feed(request):
	zeets = Zeet.objects.all()
	return render(request, 'zeets/feed.html', {'zeets':zeets})