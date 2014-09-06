from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden
from django.template import loader, RequestContext
from django.contrib import auth
from django import forms
from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
import os
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from app_drummersaransk.forms import AuthenticationCustomForm
from app_drummersaransk.forms import MyRegistrationForm, ChangePasswordForm, ChangeAvatarForm, PersonalDataForm, DrumDataForm, PathGloryForm, SearchFriendsForm, MessageForm
from app_drummersaransk.models import UserProfile, PathGlory, Friends, Gender, Status, City, Message


def custom_proc(request):
	return{
		'user': request.user,
		'request': request,
	}


@login_required	
def messages_sended_item(request, message_id):	
	message_obj = Message.get_message(message_id=message_id)
        		
	t = loader.get_template('messages_sended_item.html')
	c = RequestContext(request, {
		'message_obj': message_obj,
	}, [custom_proc])	
	
	return HttpResponse(t.render(c)) 	
	
	
@login_required	
def messages_recieve_item(request, message_id):	
	message_obj = Message.get_message(message_id=message_id)
        		
	t = loader.get_template('messages_recieve_item.html')
	c = RequestContext(request, {
		'message_obj': message_obj,
	}, [custom_proc])	
	
	return HttpResponse(t.render(c)) 	
	
	
@login_required	
def messages_recieve(request):	
	if request.method == 'POST':		
		delete_id = request.POST.get('delete_id', '')	
		try:
			Message.delete_message(delete_id)		
		except:
			return HttpResponseRedirect('/page_error404/')
			
		
	exists_recieve_messages = Message.exists_recieve_messages(request.user.id)
	messages_recieve = Message.get_recieve_messages(request.user.id)
	paginator = Paginator(messages_recieve, 10)
	list_pages = paginator.page_range
	
	page = request.GET.get('page')
	try:
		messages_recieve_paginated = paginator.page(page)
	except PageNotAnInteger:
		messages_recieve_paginated = paginator.page(1)
	except EmptyPage:
		messages_recieve_paginated = paginator.page(paginator.num_pages)	
		
	last_page = list_pages[-1]	
	first_page = list_pages[0]		
        		
	t = loader.get_template('messages_recieved.html')
	c = RequestContext(request, {
		'exists_recieve_messages': exists_recieve_messages,
		'list_pages': list_pages,
		'messages_recieve_paginated': messages_recieve_paginated,
		'last_page': last_page,
		'first_page': first_page,		
	}, [custom_proc])	
	
	return HttpResponse(t.render(c)) 	
	

@login_required	
def messages_sended(request):	
	if request.method == 'POST':		
		delete_id = request.POST.get('delete_id', '')	
		try:
			Message.delete_message(delete_id)		
		except:
			return HttpResponseRedirect('/page_error404/')
				
	exists_sended_messages = Message.exists_sended_messages(request.user.id)
	messages_sended = Message.get_sended_messages(request.user.id)
	paginator = Paginator(messages_sended, 10)
	list_pages = paginator.page_range
	
	page = request.GET.get('page')
	try:
		messages_sended_paginated = paginator.page(page)
	except PageNotAnInteger:
		messages_sended_paginated = paginator.page(1)
	except EmptyPage:
		messages_sended_paginated = paginator.page(paginator.num_pages)	
		
	last_page = list_pages[-1]	
	first_page = list_pages[0]			
        		
	t = loader.get_template('messages_sended.html')
	c = RequestContext(request, {
		'exists_sended_messages': exists_sended_messages,
		'list_pages': list_pages,
		'messages_sended_paginated': messages_sended_paginated,
		'last_page': last_page,
		'first_page': first_page,		
	}, [custom_proc])	
	
	return HttpResponse(t.render(c)) 	

	

@login_required	
def message_create(request, id_reciever=None):	
	form = MessageForm()
	obj_reciever = None
	
	if id_reciever:
		obj_reciever = UserProfile.get_entry(user_id=int(id_reciever))
		
	if request.method == 'POST':											
		form = MessageForm(request.POST)
		if form.is_valid():		
			theme = form.cleaned_data.get('theme') or None
			text = form.cleaned_data.get('text') or None
								
			Message(
				sender=request.user,
				reciever=obj_reciever,
				theme=theme,
				text=text,
			).save()
			return HttpResponseRedirect('/userprofile/message_sended/')						
        		
	t = loader.get_template('message_create.html')
	c = RequestContext(request, {
		'form': form,
		'obj_reciever': obj_reciever,
	}, [custom_proc])	
	
	return HttpResponse(t.render(c)) 	
	
	
def message_sended(request):
	t = loader.get_template('message_sended.html')
	c = RequestContext(request, {}, [custom_proc])	
	return HttpResponse(t.render(c))
		
	
def index(request):
	t = loader.get_template('page_index.html')
	c = RequestContext(request, {}, [custom_proc])	
	return HttpResponse(t.render(c))
	
	
def user(request, id):
	t = loader.get_template('page_user.html')
	c = RequestContext(request, {}, [custom_proc])	
	return HttpResponse(t.render(c))	


def login(request):
	if(request.method == "POST"):
		form = AuthenticationCustomForm(data=request.POST)		
		if form.is_valid():			
			username = request.POST.get('username', '')
			password = request.POST.get('password', '')

			user = auth.authenticate(username=username, password=password)

			if user is not None and user.is_active and username != 'admin':
				auth.login(request, user)
				return HttpResponseRedirect('/' + str(request.user.pk) + '/')
	else:
		form = AuthenticationCustomForm()	
                	
	t = loader.get_template('accounts/login.html')
	c = RequestContext(request, {
		'form': form, 
	}, [custom_proc])	
	return HttpResponse(t.render(c)) 
		
		
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/accounts/login/')
	#t = loader.get_template('accounts/logout.html')
	#c = RequestContext(request, {}, [custom_proc])	
	#return HttpResponse(t.render(c)) 		
	
	
def loggedin(request):
	t = loader.get_template('accounts/loggedin.html')
	c = RequestContext(request, {
		'full_name': request.user.username,
	}, [custom_proc])	
	return HttpResponse(t.render(c)) 	
	
	
def invalid_login(request):
	t = loader.get_template('accounts/invalid_login.html')
	c = RequestContext(request, {}, [custom_proc])	
	return HttpResponse(t.render(c)) 	
	

def registration(request):
	form = MyRegistrationForm()
	
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)	#
		if form.is_valid():
			new_user = form.save()
			
			return HttpResponseRedirect("/accounts/registration_success/")
		
		
	return render(request, "accounts/registration.html", {
		'form': form,	#
	})	
	
	
def registration_success(request):
	t = loader.get_template('accounts/registration_success.html')
	c = RequestContext(request, {}, [custom_proc])	
	return HttpResponse(t.render(c)) 				
	
	
@login_required	
def password_page(request):		
	if request.method == 'POST':								
		form = ChangePasswordForm(data=request.POST, request=request)
		if form.is_valid():
			username = User.objects.get(username__exact=request.user.username)
			username.set_password(form.cleaned_data.get('password1'))
			username.save()	
			return HttpResponseRedirect('/userprofile/password_page_changed/')						
	else:						
		form = ChangePasswordForm(request=request)
        		
	t = loader.get_template('password_page.html')
	c = RequestContext(request, {
									'form': form,
	}, [custom_proc])	
	
	return HttpResponse(t.render(c)) 	
	
	
@login_required	
def password_page_changed(request):			
	t = loader.get_template('password_page_changed.html')
	c = RequestContext(request, {}, [custom_proc])	
	return HttpResponse(t.render(c))
			
	
@login_required	
def avatar_page(request):
	try:
		entry_user_profile = UserProfile.objects.get(user_ptr_id=request.user.id)
	except:
		return HttpResponseRedirect('/page_error404/')		
			
	avatar = entry_user_profile.avatar					
	form = ChangeAvatarForm(instance=entry_user_profile)		
				
	if request.method == 'POST':								
		form = ChangeAvatarForm(request.POST, request.FILES, instance=entry_user_profile)
		if form.is_valid():				
			form.save()	
			return HttpResponseRedirect('/userprofile/avatar_page_changed/')						
        		
	t = loader.get_template('avatar_page.html')
	c = RequestContext(request, {
		'form': form,
		'avatar': avatar,
	}, [custom_proc])	
	
	return HttpResponse(t.render(c)) 	
		

@login_required	
def avatar_page_changed(request):			
	t = loader.get_template('avatar_page_changed.html')
	c = RequestContext(request, {}, [custom_proc])	
	return HttpResponse(t.render(c))	


@login_required
def personal_data_page(request):
	entry_user_profile = UserProfile.objects.get(user_ptr_id=request.user.id)
	form = PersonalDataForm(instance=entry_user_profile)

	if request.method == 'POST':
		form = PersonalDataForm(request.POST, instance=entry_user_profile)
		if form.is_valid():	
			form.save()			
			return HttpResponseRedirect('/userprofile/personal_data_page_changed/')				
	
	t = loader.get_template('personal_data_page.html')
	c = RequestContext(request, {
		'form': form,
	}, [custom_proc])
	return HttpResponse(t.render(c))  	

	
@login_required	
def personal_data_page_changed(request):			
	t = loader.get_template('personal_data_page_changed.html')
	c = RequestContext(request, {}, [custom_proc])	
	return HttpResponse(t.render(c))


@login_required
def drum_data_page(request):
	try:
		entry_user_profile = UserProfile.objects.get(user_ptr_id=request.user.id)
	except:
		return HttpResponseRedirect('/page_error404/')		
			
	drum_photo = entry_user_profile.drum_photo		
	
	form = DrumDataForm(instance=entry_user_profile)		
		
	if request.method == 'POST':
		form = DrumDataForm(request.POST, request.FILES, instance=entry_user_profile)
		if form.is_valid():			
			form.save()			
			return HttpResponseRedirect('/userprofile/drum_data_page_changed/')
	
	t = loader.get_template('drum_data_page.html')
	c = RequestContext(request, {
		'form': form,
		'drum_photo': drum_photo,	
	}, [custom_proc])
	return HttpResponse(t.render(c))  	

	
def path_glory(request, id):	
	try:
		all_user_entries = PathGlory.get_all_user_entries(id)
	except:
		return HttpResponseRedirect('/page_error404/')	
	else:	
		paginator = Paginator(all_user_entries, 10)
		list_pages = paginator.page_range
	
		page = request.GET.get('page')
		try:
			all_user_entries_paginated = paginator.page(page)
		except PageNotAnInteger:
			all_user_entries_paginated = paginator.page(1)
		except EmptyPage:
			all_user_entries_paginated = paginator.page(paginator.num_pages)	
		
	last_page = list_pages[-1]	
	first_page = list_pages[0]			
			
	t = loader.get_template('user_path_glory.html')
	c = RequestContext(request, {
		'list_pages': list_pages,
		'all_user_entries_paginated': all_user_entries_paginated,
		'last_page': last_page,
		'first_page': first_page,
	}, [custom_proc])	
	return HttpResponse(t.render(c))
	
		
@login_required	
def drum_data_page_changed(request):			
	t = loader.get_template('drum_data_page_changed.html')
	c = RequestContext(request, {}, [custom_proc])	
	return HttpResponse(t.render(c))


@login_required	
def path_glory_edit(request):	
	if request.method == 'POST':
		delete_id = request.POST.get('delete_id', None).strip()
		try:
			PathGlory.delete_entry(delete_id)		
		except:
			return HttpResponseRedirect('/page_error404/')		
			
	all_user_entries = PathGlory.get_all_user_entries(request.user.pk)
	paginator = Paginator(all_user_entries, 10)
	list_pages = paginator.page_range
	
	page = request.GET.get('page')
	try:
		all_user_entries_paginated = paginator.page(page)
	except PageNotAnInteger:
		all_user_entries_paginated = paginator.page(1)
	except EmptyPage:
		all_user_entries_paginated = paginator.page(paginator.num_pages)	
		
	last_page = list_pages[-1]	
	first_page = list_pages[0]		
		
	t = loader.get_template('path_glory_edit.html')
	c = RequestContext(request, {
		'list_pages': list_pages,
		'all_user_entries_paginated': all_user_entries_paginated,
		'last_page': last_page,
		'first_page': first_page,			
	}, [custom_proc])	
	return HttpResponse(t.render(c))
	

@login_required	
def path_glory_add_item(request):	
	if request.method == 'POST':
		form = PathGloryForm(request.POST, request.FILES)
		if form.is_valid():	
			PathGlory(
				user_id=form.cleaned_data.get('user_id'), 
				title=form.cleaned_data.get('title').strip(), 
				date=form.cleaned_data.get('date'), 
				place=form.cleaned_data.get('place').strip(), 
				teaser=form.cleaned_data.get('teaser').strip(), 
				text=form.cleaned_data.get('text').strip(), 
				path_glory_photo=form.cleaned_data.get('path_glory_photo'), 
			).save()				
												
			return HttpResponseRedirect('/userprofile/path_glory_add_item_added/')
	else:			
		form = PathGloryForm(initial={
			'user_id': request.user.pk,
		})
		
	t = loader.get_template('path_glory_add_item.html')
	c = RequestContext(request, {
		'form': form,		
	}, [custom_proc])	
	return HttpResponse(t.render(c))
		
		
@login_required	
def path_glory_edit_item(request, id):	
	entry = PathGlory.get_entry_short(id=id)
	path_glory_photo = entry.path_glory_photo
		
	if request.method == 'POST':
		form = PathGloryForm(request.POST, request.FILES, instance=entry)
		if form.is_valid():		
			form.save()		
			return HttpResponseRedirect('/userprofile/path_glory_edit_item_changed/')
	else:				
		form = PathGloryForm(instance=entry)	
		
	t = loader.get_template('path_glory_edit_item.html')
	c = RequestContext(request, {
		'form': form,
		'id': id,	
		'path_glory_photo': path_glory_photo,	
	}, [custom_proc])	
	return HttpResponse(t.render(c))	
	
	
@login_required	
def path_glory_edit_item_changed(request):			
	t = loader.get_template('path_glory_edit_item_changed.html')
	c = RequestContext(request, {}, [custom_proc])	
	return HttpResponse(t.render(c))	
	
	
@login_required	
def path_glory_add_item_added(request):			
	t = loader.get_template('path_glory_add_item_added.html')
	c = RequestContext(request, {}, [custom_proc])	
	return HttpResponse(t.render(c))	
	

@login_required	
def user_path_glory_page(request, id, id_p):
	try:
		entry = PathGlory.get_entry(id, id_p=id_p)
	except:
		return HttpResponseRedirect('/page_error404/')		
		
	t = loader.get_template('user_path_glory_page.html')
	c = RequestContext(request, {
		'entry': entry,
	}, [custom_proc])	
	return HttpResponse(t.render(c))	
	

@login_required		
def user_personal(request, id):		
	try:
		entries_user_profile = UserProfile.objects.get(user_ptr_id=id)
	except:
		return HttpResponseRedirect('/page_error404/')

	entries_user = User.objects.get(id=id)
	
	path_pk = ''
	
	if request.method == 'POST':	
		path_pk = id
		user_id = int(request.user.pk)
		
		if request.POST.get('action', '') == 'add':					
			q = Friends.get_entry(user_id=user_id, friend_id=path_pk)		
			
			if q == False:				
				Friends.set_entry(user_id=user_id, friend_id=path_pk)	#add							
				
		if request.POST.get('action', '') == 'delete':		
			try:
				Friends.get_entry(user_id=user_id, friend_id=path_pk)	#del
			except:
				pass			
			else:			
				Friends.del_entry(user_id=user_id, friend_id=path_pk)
			
	t = loader.get_template('user_personal.html')
	c = RequestContext(request, {
		'login': entries_user.username,
		'entries_user_profile': entries_user_profile,
	}, [custom_proc])	
	return HttpResponse(t.render(c))	
	

@login_required	
def user_druminfo(request, id):	
	try:
		entries_user_profile = UserProfile.objects.get(user_ptr_id=id)
	except:
		return HttpResponseRedirect('/page_error404/')	
		
	t = loader.get_template('user_druminfo.html')
	c = RequestContext(request, {
		'entries_user_profile': entries_user_profile,
	}, [custom_proc])	
	return HttpResponse(t.render(c))			


def page_error404(request):	
	t = loader.get_template('page_error404.html')
	c = RequestContext(request, {}, [custom_proc])	
	return HttpResponse(t.render(c))			


@login_required	
def friends_action(request, path, user_pk):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)	#
		if form.is_valid():
			new_user = form.save()
			
			return HttpResponseRedirect("/accounts/registration_success/")
			
			
@login_required	
def friends_list_edit(request, friend_id=None):	
	if friend_id:
		Friends.del_entry(user_id=request.user.id, friend_id=friend_id)
		
	all_entries = Friends.get_all_entries(user_id=request.user.id)
	count_friends = Friends.count_entry(user_id=request.user.id)
	exists_entry = Friends.exists_entry(user_id=request.user.id)
	
	t = loader.get_template('user_friends_list.html')
	c = RequestContext(request, {
		'all_entries': all_entries,
		'count_friends': count_friends,
		'flag_buttons_visibility': True,
		'exists_entry': exists_entry,
	}, [custom_proc])	
	return HttpResponse(t.render(c))				


@login_required	
def user_friends_list(request, id):		
	all_entries = Friends.get_all_entries(user_id=id)
	count_friends = Friends.count_entry(user_id=id)
	exists_entry = Friends.exists_entry(user_id=request.user.id)
	
	t = loader.get_template('user_friends_list.html')
	c = RequestContext(request, {
		'all_entries': all_entries,
		'count_friends': count_friends,
		'flag_buttons_visibility': False,
		'exists_entry': exists_entry,
	}, [custom_proc])	
	return HttpResponse(t.render(c))	


@login_required	
def friends_search(request):
	search_result = None
	form = SearchFriendsForm()
	my_friends = []
	
	if request.method == 'POST':
		form = SearchFriendsForm(request.POST)
		if form.is_valid():	
			name = request.POST.get('name', None).strip()
			birth_date = request.POST.get('birth_date', None)
			gender = request.POST.get('gender', None).strip()
			status = request.POST.get('status', None).strip()			
			city = request.POST.get('city', None).strip()	
			city_ids = City.get_city_ids(city)	
			my_friends = Friends.get_friends_ids(request.user.id)			
						
			search_result = UserProfile.objects.all()
			
			if name:
				search_result = search_result.filter(Q(nickname__icontains=name.strip()) | Q(family__icontains=name.strip()) | Q(name1__icontains=name.strip()) | Q(name2__icontains=name.strip()))  
				
			if birth_date:
				search_result = search_result.filter(birth_date=birth_date)

			if gender:
				search_result = search_result.filter(gender=gender)		

			if status:
				search_result = search_result.filter(status=status)
				
			if my_friends:
				search_result = search_result.exclude(id__in=my_friends)
				search_result = search_result.exclude(id__in=[request.user.id])				

			if city:	
				if city_ids:
					search_result = search_result.filter(city__in=city_ids)				
				else:
					search_result = None
					

							
			if not search_result:
				search_result = 'По вашему запросу ничего не найдено.'		
				
	if isinstance(search_result, str):
		search_result_type = 'str'
	elif isinstance(search_result, dict):
		search_result_type = 'dict'
	else:
		search_result_type ='none'						

	t = loader.get_template('friends_search.html')
	c = RequestContext(request, {
		'form': form,
		'search_result': search_result,
		'search_result_type': search_result_type,
	}, [custom_proc])	
	return HttpResponse(t.render(c))	
	
	
