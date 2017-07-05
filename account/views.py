# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import Profile
from .forms import UserRegisterForm, UserEditForm, ProfileEditForm

@login_required
def dashboard(request):
	template = 'account/dashboard.html'
	return render(request, template)	

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
			messages.success(request, 'Profile updated successfully')
	else:
		user_form = UserEditForm(instance = request.user)
		profile_form = ProfileEditForm(instance = request.user.profile)
	return render(request, 'account/edit.html', {'user_form':user_form, 'profile_form':profile_form})