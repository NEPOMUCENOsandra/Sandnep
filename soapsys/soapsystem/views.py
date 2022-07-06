
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect


#from soapsys.soapsys.settings import INSTALLED_APPS
from .models import *

installed_apps = ['soapsystem']

def Mainpage(request):
	return render(request,'soapsystem/mainpage.html')

def Aboutshop(request):
	return render(request,'soapsystem/aboutshop.html')

def Soaps(request):
	return render(request,'soapsystem/soaps.html')

def SoapBuy(request):
	if request.method == "POST":
		soapname = request.POST['soapname']
		qty = request.POST['qty']
		soap = SoapBuy(soapname = soapname,
		qty = qty,
		)
		
		soap.save()
		return render(request,'soapsystem/Soapbuy.html')
	else:
		soapss =   SoapBuy.objects.all()
		return render(request,'soapsystem/new.html',{'soapss':soapss})

def Topay(request):
	if request.method == "POST":
		street = request.POST['street']
		subd = request.POST['subd']
		brgy = request.POST['brgy']
		city = request.POST['city']
		zipcode = request.POST['zipcode']
		pay = Topay(street = street,
		subd = subd,
		brgy = brgy,
		city = city,
		zipcode = zipcode,
		)
		
		pay.save()
		return render(request,'soapsystem/topay.html')
	else:
		payment =   Topay.objects.all()
		return render(request,'soapsystem/topay.html',{'payment':payment})
	



def ContactForm(request):
	return render(request,'soapsystem/contactform.html')

def Feedback(request):
	return render(request,'soapsystem/feedback.html')


def buyerinfor(request):
	if request.method == "POST":
		lastname = request.POST['lastname']
		firstname = request.POST['firstname']
		middlename = request.POST['middlename']
		contact = request.POST['contact']
		email = request.POST['email']
		buyer = Buyerinfor(lastname = lastname,
		firstname = firstname,
		middlename = middlename,
		contact = contact,
		email = email,
		)
		
		buyer.save()
		return render(request,'soapsystem/new.html')
	else:		
		buyerss =   Buyerinfor.objects.all()
		return render(request,'soapsystem/snew.html',{'buyerss':buyerss})