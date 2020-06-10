import sys
import os
import json
from django.shortcuts import render, redirect, reverse, \
						get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, \
						JsonResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib import auth
from django.core.mail import EmailMultiAlternatives

from main_project.forms import RegisterUser
from main_project.models import Blog, Report,ContactForm


# Create your views here.

def index(request):

	message_success_message_to_show = 'false'   #because it will use in js so f small. Also will not use it as a str so can use it as if condition

	if request.method == 'POST':
		try:
			ContactForm.objects.create(
				fullname=request.POST['input_fullname'],
				email=request.POST['input_email'],
				subject=request.POST['input_subject'],
				message=request.POST['input_message'],
			)

			message_success_message_to_show = 'true'  #because it will use in js so t small. Also will not use it as a str so can use it as if condition
		except Exception as e:
			print(e)
			pass


	context = {
		'message_success_message_to_show':message_success_message_to_show,
	}

	return render(request, 'index.html', context)


def service(request):
	
	blogs = Blog.objects.all()[:5]

	context = {
		'blogs':blogs
	}

	return render(request, 'service.html', context)


def about(request):

	blogs = Blog.objects.all()[:5]

	context = {
		'blogs':blogs
	}

	return render(request, 'about.html', context)


@login_required(login_url=settings.LOGIN_URL)
def client(request):
	
	if request.method == 'POST':
		try:
			values = json.loads(request.body)
			email_to_send = values['email_to_send']
			if email_to_send == "":
				email_to_send = settings.SEND_EMAIL_TO

			for value in values['value']:
				print(
						values['value'][value]['date'],
						values['value'][value]['turn'],
						values['value'][value]['period_from'],
						values['value'][value]['period_to'],
						values['value'][value]['local_sold'],
						values['value'][value]['amount_sold'],
					)
				Report.objects.create(
						date=values['value'][value]['date'],
						turn=values['value'][value]['turn'],
						period_from=values['value'][value]['period_from'],
						period_to=values['value'][value]['period_to'],
						local_sold=values['value'][value]['local_sold'],
						amount_sold=values['value'][value]['amount_sold'],
						user=request.user
					)

			subject = 'Hi! Got a new report'
			text_content = 'Report From '+ str(request.user)
			from_email = settings.SEND_EMAIL_FROM  # no need auto generate from setting EMAIL_HOST_USER
			body_html_content = str(values['html_content'])
			to = [email_to_send, 'mjmarronzinho@gmail.com']
			msg = EmailMultiAlternatives(subject, text_content, from_email, to)
			msg.attach_alternative(body_html_content, "text/html")
			msg.send()


			return JsonResponse('saved', safe=False)
		except Exception as e:
			print('')
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			print(e, exc_type, fname, exc_tb.tb_lineno)
			print('')
			return JsonResponse('not saved', safe=False)

	blogs = Blog.objects.all()[:5]

	context = {
		'blogs':blogs
	}

	return render(request, 'client.html', context)


def blog(request):
	blogs = Blog.objects.all()

	context = {
		'blogs' : blogs
	}

	return render(request, 'blog.html', context)


def single_blog(request, blog_id):
	
	blog = get_object_or_404(Blog, id=blog_id)
	context = {
		'blog' : blog
	}

	return render(request, 'single_blog.html', context)


def sign_in(request):

	register_form = RegisterUser()
	login_errors = []
	start_with_login_tab = 'false'
	if request.method == 'POST':
		if request.POST['submit'] == 'register_form':
			register_form = RegisterUser(request.POST)
			if register_form.is_valid():
				user = register_form.save()
				
				try:
					auth.login(request, user)
				except Exception as e:
					print('user can\'t logged in after register')
				return redirect('main_project:index')
		if request.POST['submit'] == 'sign_in_form':
			username = request.POST['username']
			password = request.POST['password']

			
			user = auth.authenticate(username=username, password=password)
			if user is not None:
				auth.login(request, user)
				return redirect('main_project:index')
			else:
				print('error logged in')
				start_with_login_tab = 'true'
				login_errors.append('Please enter the correct username and password. Note that password field is case-sensitive.')


			




	context = {
		'register_form' : register_form,
		'login_errors': login_errors,
		'start_with_login_tab' : start_with_login_tab
	}

	return render(request, 'sign_in.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('main_project:index'))
