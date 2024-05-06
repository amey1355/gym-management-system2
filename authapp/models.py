from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
	name=models.CharField(max_length=25)
	email=models.EmailField()
	phnumber=models.IntegerField(max_length=12)
	description=models.TextField(max_length=500)
	
	def __str__(self):
		return self.email

class Enrollment(models.Model):
	FullName=models.CharField(max_length=25)
	Email=models.EmailField()
	Gender=models.CharField(max_length=25)
	PhoneNumber=models.IntegerField(max_length=12)
	DOB=models.CharField(max_length=50)
	SelectMembershipplan=models.CharField(max_length=200)
	SelectTrainer=models.CharField(max_length=55)
	Reference=models.CharField(max_length=55)
	Address=models.TextField(max_length=200)
	PaymentStatus=models.CharField(max_length=55,blank=True,null=True)
	Price=models.IntegerField(max_length=55,blank=True,null=True)
	DueDate=models.DateTimeField(blank=True,null=True)
	TimeStamp=models.DateTimeField(auto_now_add=True,blank=True)
	JoiningDate=models.DateTimeField(blank=True,null=True)

	def __str__(self):
		return self.FullName
class Trainer(models.Model):
	name=models.CharField(max_length=55)
	gender=models.CharField(max_length=25)
	phone=models.IntegerField(max_length=12)
	salary=models.IntegerField(max_length=25)
	TimeStamp=models.DateTimeField(auto_now_add=True,blank=True)

	
	def __str__(self):
		return self.name

class MembershipPlan(models.Model):
	plan=models.CharField(max_length=185)
	price=models.IntegerField(max_length=55)
	
	
	def __int__(self):
		return self.id	#bydefault table cha id return karnaar
class Gallery(models.Model):
	title=models.CharField(max_length=100)
	img=models.ImageField(upload_to="gallery")
	timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
	def __int__(self):
		return self.id

class Attendance(models.Model):
	Selectdate=models.DateTimeField(auto_now_add=True)
	Email=models.EmailField()
	Login=models.CharField(max_length=200)
	Logout=models.CharField(max_length=200)
	SelectWorkout=models.CharField(max_length=200)
	TrainedBy=models.CharField(max_length=200)
	def __int__(self):
		return self.id

# Subscription Plan
class SubPlan(models.Model):
	title=models.CharField(max_length=150)
	price=models.IntegerField(max_length=50)
	highlight_status=models.BooleanField(default=False,null=True)

	def __str__(self):
		return f"{self.title} - {self.price} - {self.highlight_status}"

#Subscription Plan Features
class SubPlanFeature(models.Model):
	#subplan=models.ForeignKey(SubPlan,on_delete=models.CASCADE)	#relationship dakavtayt plan ani features chi
	subplan=models.ManyToManyField(SubPlan)
	title=models.CharField(max_length=150)
	
	def __str__(self):
		return f"{self.title}"

class PlanDiscount(models.Model):
	subplan=models.ForeignKey(SubPlan,on_delete=models.CASCADE,null=True)
	total_months=models.IntegerField()
	total_discount=models.IntegerField()

	def __str__(self):
		return str(self.total_months)

class Subscriber(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	mobile=models.CharField(max_length=20)
	address=models.TextField()
	img=models.ImageField(upload_to="subs/")

	def __str__(self):
		return str(self.user)
	def image_tag(self):
		return mark_safe('<img src="%s" width="80" />' % (self.img.url)) 

class Subscription(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	plan=models.ForeignKey(SubPlan,on_delete=models.CASCADE,null=True)
	price=models.CharField(max_length=50)

	def __str__(self):
		return str(self.plan)
	