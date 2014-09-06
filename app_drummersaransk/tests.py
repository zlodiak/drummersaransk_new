from django.test import TestCase
from django.test.client import Client
from app_drummersaransk.forms import AuthenticationCustomForm


class TestTemplatePage(TestCase):
	'''
		check template for login, registration page
	'''

	def set_up(self):
		self.client = Client()
		user = User.objects.create('qqq', 'qqq')
	'''
	def test_login_page(self):
		response = self.client.get('/accounts/login/')
		self.assertTemplateUsed(response, 'accounts/login.html')
		self.assertTemplateUsed(response, 'page_base.html')
		
	def test_registration_page(self):
		response = self.client.get('/accounts/registration/')
		self.assertTemplateUsed(response, 'accounts/registration.html')			
		self.assertTemplateUsed(response, 'page_base.html')	'''
		
	def test_logged_in(self):
		self.client.login(username='qqq', password='qqq')
		response = self.client.post('/2/')
		self.assertTemplateUsed(response, 'user_personal.html')
		
	#def test_forms(self):
		#form_data = {'username': 'qqq', 'password': 'qqq'}
		#form = AuthenticationCustomForm(data=form_data)
		#self.assertEqual(form.is_valid(), True)
	
		


