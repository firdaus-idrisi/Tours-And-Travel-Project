from django.shortcuts import render
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages 
from django.contrib.auth import login, authenticate,logout 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep


def index(request):
    return render(request,"index.html")
def index2(request):
	return render(request,'index2.html')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
		
	form = NewUserForm()
    # return render(request,"index.html")

	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index2")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()

	return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
	return index(request)
	 

def Contact(request):
	return render(request,"Contact.html")
	 

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password_reset_email.txt"
					c = {
						"email":user.email,
						'domain':'127.0.0.1:8000',
						'site_name': 'Tours and Travels',
						"uid": urlsafe_base64_encode(force_bytes(user.pk)),
						"user": user,
						'token': default_token_generator.make_token(user),
						'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					sender_email = ''
					sender_password = 'Welcome@123##'
					try:
						s = smtplib.SMTP(host='smtp.office365.com', port=587)
						s.starttls()
						s.login(sender_email, sender_password)
						sleep(2)
						print("Login Done")
						# send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')

					msg = MIMEMultipart()
					message = email
					msg['From']=sender_email
					msg['To']= user.email
					msg['Subject']= subject
					msg.attach(MIMEText(message, 'plain'))
					s.send_message(msg)
					print("Mail Sent")
					messages.success(request, 'Email for Reset Password has been sent.')
			else:
				                # print("entered in else case")
				messages.error(request, 'An invalid email has been entered.')
				

			return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password_reset.html", context={"password_reset_form":password_reset_form})