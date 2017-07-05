# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
from .models import Zeet
from .forms import ZeetPostForm

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
			return redirect('zeets:home')
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

