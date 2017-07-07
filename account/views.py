# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.http import JsonResponse
from django.views.decorators.http import require_POST


from .models import Profile, Contact 
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

@login_required
def user_list(request):
	users = User.objects.filter(is_active = True)
	return render(request, 'account/list.html', {'users':users})

@login_required
def user_detail(request, username):
	user = get_object_or_404(User, username = username, is_active = True)
	return render(request, 'account/detail.html', {'user':user})

@require_POST
@login_required
def user_follow(request):
	user_id = request.POST.get('id')
	action = request.POST.get('action')
	if user_id and action:
		try:
			user = User.objects.get(id = user_id)
			if action == 'follow':
				Contact.objects.get_or_create(user_from = request.user, user_to = user)
				return redirect('account:user_detail', user.username)
			else:
				Contact.objects.filter(user_from = request.user, user_to = user).delete()
				return redirect('account:user_detail', user.username)
			return JsonResponse({'status':'ok'})
		except User.DoesNotExist:
			return JsonResponse({'status':'ko'})
	return JsonResponse({'status':'ko'})