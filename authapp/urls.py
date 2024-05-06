#from django.contrib import admin
from django.urls import path
from authapp import views
urlpatterns = [
    path("",views.Home,name="Home"),
    path("signup",views.signup,name="signup"),
    path("login",views.handlelogin,name="handlelogin"),
    path("urnp",views.urnp,name="urnp"),
    path("logout",views.handlelogout,name="handlelogout"),
    path("contact",views.contact,name="contact"),
    path("pricing",views.pricing,name="pricing"),
    path('checkout/<int:plan_id>',views.checkout,name="checkout"),
    #path("checkout",views.checkout,name="checkout"),	
    path("join",views.enroll,name="enroll"),
    path("vprofile",views.profile,name="profile"),
    path('gallery',views.gallery,name="gallery"),
    path('attendance',views.attendance,name="attendance"),
    path('checkout_session/<int:plan_id>',views.checkout_session,name="checkout_session"),		
    path('pay_success',views.pay_success,name="pay_success"),
    path('pay_cancel',views.pay_cancel,name="pay_cancel"),	
]
