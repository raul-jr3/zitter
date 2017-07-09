# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.http import JsonResponse
from django.views.decorators.http import require_POST


from zeets.models import Zeet 
from .models import Profile
from .forms import UserRegisterForm, UserEditForm, ProfileEditForm

@login_required
def dashboard(request):
	zeets = Zeet.objects.filter(zeeter = request.user)
	template = 'account/dashboard.html'
	return render(request, template, {'zeets':zeets})	

def register(request):
	if request.method == 'POST':
		form =UserRegisterForm(data = request.POST)
		if form.is_valid():
			new_user = form.save(commit = False)
			new_user.set_password(form.cleaned_data['password'])
			new_user.save()
			profile = Profile.objects.create(user = new_user)
			messages.success(request, 'User registered successfully')
			return render(request, 'account/register_done.html', {'new_user':new_user})
	else:
		form = UserRegisterForm()
	return render(request, 'account/register.html', {'form':form})

@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(data = request.POST, instance = request.user)
		profile_form = ProfileEditForm(data = request.POST, instance = request.user.profile, files = request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return redirect('account:dashboard')
	else:
		user_form = UserEditForm(instance = request.user)
		profile_form = ProfileEditForm(instance = request.user.profile)
	return render(request, 'account/edit.html', {'user_form':user_form, 'profile_form':profile_form})

@login_required
def users_list(request):
	users = User.objects.all().exclude(username = request.user.username)
	return render(request, 'account/users_list.html', {'users':users})

@login_required
def user_detail(request, username):
	user = get_object_or_404(User, username = username, is_active = True)	
	zeets = Zeet.objects.filter(zeeter = user)
	return render(request, 'account/detail.html', {'zeets':zeets, 'user':user})

