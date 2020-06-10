from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.

class Report(models.Model):

	period_choice = (

				('12.00 AM','12.00 AM'), ('1.00 AM','1.00 AM'),
				('2.00 AM','2.00 AM'), ('3.00 AM','3.00 AM'),
				('4.00 AM','4.00 AM'), ('5.00 AM','5.00 AM'),
				('6.00 AM','6.00 AM'), ('7.00 AM','7.00 AM'),
				('8.00 AM','8.00 AM'), ('9.00 AM','9.00 AM'),
				('10.00 AM','10.00 AM'), ('11.00 AM','11.00 AM'),
				('12.00 PM','12.00 PM'), ('1.00 PM','1.00 PM'),
				('2.00 PM','2.00 PM'), ('3.00 PM','3.00 PM'),
				('4.00 PM','4.00 PM'), ('5.00 PM','5.00 PM'),
				('6.00 PM','6.00 PM'), ('7.00 PM','7.00 PM'),
				('8.00 PM','8.00 PM'), ('9.00 PM','9.00 PM'),
				('10.00 PM','10.00 PM'), ('11.00 PM','11.00 PM')
			)


	date = models.CharField(max_length=200, null=True, blank=True)
	turn = models.IntegerField(null=True, blank=True)
	period_from = models.CharField(max_length=200, null=True, blank=True, choices=period_choice)
	period_to = models.CharField(max_length=200, null=True, blank=True, choices=period_choice)
	local_sold = models.CharField(max_length=20, null=True, blank=True)
	amount_sold = models.IntegerField(null=True, blank=True)
	time = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return str(self.user)


class Blog(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=300, null=True, blank=False)
	text = models.TextField(max_length=30, null=True, blank=False) #just as a intro
	content = RichTextUploadingField()
	time = models.DateTimeField(auto_now=True)


	def __str__(self):
		return str(self.user)

class ContactForm(models.Model):
	fullname = models.CharField(max_length=100, null=True, blank=False)
	email = models.CharField(max_length=100, null=True, blank=False)
	subject = models.CharField(max_length=300, null=True, blank=False)
	message = models.CharField(max_length=1000, null=True, blank=False)
	time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.fullname)


