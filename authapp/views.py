from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from random import *
from django.core.mail import send_mail
from authapp.models import Contact,MembershipPlan,Trainer,Enrollment,Gallery,Attendance, SubPlan,SubPlanFeature
import stripe

# Create your views here.
def Home(request):
	"""if request.user.is_authenticated:
		return redirect('/')
	else:
		return render(request,"signup.html")"""
	return render(request,"index.html")

def profile(request):
	if not request.user.is_authenticated:
		messages.warning(request,"Please Login and Try Again")
		return redirect("/login")
	user_email=request.user
	posts=Enrollment.objects.filter(Email=user_email)	#joh apla user cha email id aahe tyala database madhlya email id chi match karnaar ani mag filter karun tya particular user cha profile disnaar
	attendance=Attendance.objects.filter(Email=user_email)
	print(posts)
	print(attendance)
	context={"posts":posts,"attendance":attendance}
	return render(request,"profile.html",context)
	
def urnp(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method=="POST":
			email=request.POST.get("email")
			try:
				usr=User.objects.get(username=email)
				pass1=randint(10000,99999)
				print(pass1)
				usr.set_password(str(pass1))
				usr.save()
				subject="Do Not Share OTP With Anyone"
				text="Your New Password is  "+str(pass1)
				from_email="tester.vivek.2march23@gmail.com"
				to_email=[str(email)]
				send_mail(subject,text,from_email,to_email)
				messages.success(request, 'Password Sent successful. Check your email for the new password.')
				return redirect('/login')
			except User.DoesNotExist:
				messages.error(request, 'User not registered. Please try again.')
				return render(request,"urnp.html")
				
		else:
			return render(request,"urnp.html")

def generate_otp():
	return str(randint(10000, 99999))

def signup(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == "POST":
			email = request.POST.get("email")
			pass1 = generate_otp()
			try:
				user = User.objects.get(username=email)
				messages.warning(request, "Email already in use")
				return redirect('/signup')
			except User.DoesNotExist:
				user = User.objects.create_user(username=email, password=pass1)

                		# Send the OTP via email
				subject = 'Your OTP for Signup'
				message = f'Your OTP is: {pass1}. Use this OTP as your password.'
				from_email = 'tester.vivek.2march23@gmail.com'
				recipient_list = [email]

				send_mail(subject, message, from_email, recipient_list)
				messages.success(request, "User is Created. Please check your email for Password.")
				return redirect("/login")
		else:
			return render(request, "signup.html")
	
def handlelogin(request):
	"""if request.user.is_authenticated:
		return redirect('/')
	else:"""
	if request.method=="POST":
			#pno=request.POST.get("usernumber")
		email=request.POST.get("email")
		pass1=request.POST.get("pass1")
		usr=authenticate(username=email,password=pass1)
		if usr is not None:
			login(request,usr)
			messages.success(request, "Login successful")
			return redirect("/")		
		else:
			messages.warning(request,"check the details again")
			return redirect('/login')			
	return render(request,"handlelogin.html")

def handlelogout(request):
	logout(request)
	messages.info(request,"Successfully Logout")
	return redirect('/login')
def contact(request):
	if request.method=="POST":
		name=request.POST.get("name")
		email=request.POST.get("email")
		number=request.POST.get("number")
		desc=request.POST.get("desc")
		myquery=Contact(name=name,email=email,phnumber=number,description=desc)
		myquery.save()
		messages.info(request,"Success,your data has been saved we will reach out to you soon")
		return redirect('/contact')

	return render(request,"contact.html")

def pricing(request):
	if not request.user.is_authenticated:
		messages.warning(request,"Please Login and Try Again")
		return redirect("/login")

	pricing=SubPlan.objects.all()
	dfeatures=SubPlanFeature.objects.all()
	context={'plans':pricing,'dfeatures':dfeatures}
	return render(request,"pricing.html",context)

def checkout(request,plan_id):
	planDetail=SubPlan.objects.get(pk=plan_id)
	context={'plan':planDetail}
	return render(request,'checkout.html',context)
"""def checkout(request):
	return render(request,"checkout.html")"""
	

def enroll(request):
	if not request.user.is_authenticated:
		messages.warning(request,"Please Login and Try Again")
		return redirect("/login")

	Membership=MembershipPlan.objects.all()
	selecttrainer=Trainer.objects.all()
	context={"Membership":Membership,"selecttrainer":selecttrainer}
	if request.method=="POST":
		FullName=request.POST.get("FullName")
		email=request.POST.get("email")
		gender=request.POST.get("gender")
		PhoneNumber=request.POST.get("PhoneNumber")
		DOB=request.POST.get("DOB")
		member=request.POST.get("member")
		trainer=request.POST.get("trainer")
		reference=request.POST.get("reference")
		address=request.POST.get("address")
		myquery=Enrollment(FullName=FullName,Email=email,Gender=gender,PhoneNumber=PhoneNumber,DOB=DOB,SelectMembershipplan=member,SelectTrainer=trainer,Reference=reference,Address=address)	#hyat left vala variable database madhla naav aahe ani right vala varable form che inputs ghetana che naav aahe je apan html file madhe name madhe gheto te
		myquery.save()
		messages.success(request,"Thanks for Enrollment!!")
		return redirect('/join')
	return render(request,"enroll.html",context)

def gallery(request):
	posts=Gallery.objects.all()
	context={"posts":posts}
	return render(request,"gallery.html",context)

def attendance(request):
	if not request.user.is_authenticated:
		messages.warning(request,"Please Login and Try Again")
		return redirect("/login")
	selecttrainer=Trainer.objects.all()
	context={"selecttrainer":selecttrainer}
	if request.method=="POST":
		Email=request.POST.get("email")	#get madhe je form madhe id mahnun ghetlay te lihto apppan ani left variable aahe toh models madhlach aahe
		SelectWorkout=request.POST.get("workout")
		Login=request.POST.get("logintime")
		Logout=request.POST.get("loginout")
		TrainedBy=request.POST.get("trainer")
		query=Attendance(Email=Email,SelectWorkout=SelectWorkout,Login=Login,Logout=Logout,TrainedBy=TrainedBy)
		query.save()
		messages.success(request,"Attendance Applied Successfully")
		return redirect('/attendance')
	return render(request,"attendance.html",context)
	

stripe.api_key='sk_test_51OwqxzSCPbfJjXXtuNbGQYMyS9vclIx2MsCtN6NfXJ4sTB9yff4DVFZyD7LkPXoLmrhnL3aAsVUZcNwrWpXPujn200EidgXz7o'
def checkout_session(request,plan_id):
	plan=SubPlan.objects.get(pk=plan_id)
	session=stripe.checkout.Session.create(
		payment_method_types=['card'],
		line_items=[{
			'price_data': {
				'currency': 'inr',
				'product_data': {
					'name': plan.title,
				},
				'unit_amount': plan.price*100,	#hyat paise la rupee madhe convert kelay 100paise=1rupee
			},
			'quantity':1,
		}],
		mode='payment',
		success_url='http://127.0.0.1:8000/pay_success',
		cancel_url='http://127.0.0.1:8000/pay_cancel',
	)
	return redirect(session.url,code=303)	

def pay_success(request):
	return render(request,"success.html")

def pay_cancel(request):
	return render(request,"cancel.html")	
			