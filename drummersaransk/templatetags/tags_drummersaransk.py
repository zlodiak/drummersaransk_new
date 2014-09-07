from django import template
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.conf import settings
import re
import os

from app_drummersaransk.models import Friends, UserProfile, Message
from drummersaransk.utils import compare_ids

register = template.Library()
    

@register.inclusion_tag("part_nav_edit.html")
def part_nav_edit(user, request):
	ids_data = compare_ids(request)
	new_sends = Message.get_new_sends(user.pk)
			
	return{
		'flag_homepage': ids_data['flag_homepage'],
		'user_pk': user.pk,
		'is_authenticated': user.is_authenticated,
		'new_sends': new_sends,
	}
	
	
@register.inclusion_tag("part_nav_basic.html")
def part_nav_basic(user_pk, request):
	if 'cookie_user_pk' in request.COOKIES:
		user_pk = request.COOKIES['cookie_user_pk']
		
	search = re.search('^\/(?P<slug>[0-9]+?)\/.*', request.path)
	if search is not None:
		user_pk = search.group(1)	
		response = HttpResponse()
		response.set_cookie( 'cookie_user_pk', user_pk )
		
	if not request.user.is_authenticated():
		user_pk = 'index'

	try:
		username = UserProfile.objects.get(user_ptr_id=user_pk)
	except:
		username = None
		
	return{
		'user_pk': user_pk,
		'username': username,
		'is_authenticated': request.user.is_authenticated(),
	}
	
	
@register.inclusion_tag("part_auth_area.html")
def part_auth_area(is_authenticated):
	return {
		'is_authenticated': is_authenticated,
	}	
	
	
@register.inclusion_tag("auth_area_logged_in.html")
def logged_in(username):	
	return{
		'auth_name': username,
	}
	
	
@register.inclusion_tag("auth_area_logged_out.html")
def logged_out():	
	return	
	
	
@register.inclusion_tag("right_col.html")
def right_col():	
	return	
	
	
@register.inclusion_tag("part_friends_buttons_area.html")
def friends_buttons_area(request):	
	flag_friend = True

	ids_data = compare_ids(request)
			
	flag_friend = Friends.get_entry(user_id=request.user.pk, friend_id=ids_data['path_pk'])
				
	return {
		'flag_homepage': ids_data['flag_homepage'],
		'flag_friend': flag_friend,
	}
	
	
@register.inclusion_tag("part_message_buttons_area.html")
def message_buttons_area(request):	
	ids_data = compare_ids(request)
	
	if int(request.user.pk) == int(ids_data['path_pk']):
		flag_show_message_button = False
	else:
		flag_show_message_button = True
				
	return {
		'id_reciever': ids_data['path_pk'],
		'flag_show_message_button': flag_show_message_button,
	}			
	
	
@register.inclusion_tag("user_friend_item.html")
def friend_item(friend_id, flag_buttons_visibility):	
	try:
		user_info = UserProfile.objects.get(user_ptr_id=friend_id)
	except:
		return False
	else:
		return{
			'user_info': user_info,
			'flag_buttons_visibility': flag_buttons_visibility,
		}
	
	

