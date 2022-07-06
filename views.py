from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

def Mainpage(request):
	return render(request,'mainpage.html')

def Aboutshop(request):
	return render(request,'aboutshop.html')

def Soaps(request):
	return render(request,'soaps.html')

def SoapBuy(request):
	if request.method == "POST":
		soapname = request.POST['soapname']
		qty = request.POST['qty']
		soap = SoapBuy(soapname = soapname,
		qty = qty,
		)
		
		soap.save()

	else:
		return render(request,'Soapbuy.html')
	soapss =   SoapBuy.objects.all()
	return render(request,'new.html',{'soapss':soapss})

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

	else:
		payment =   Topay.objects.all()
		return render(request,'topay.html',{'payment':payment})
	



def ContactForm(request):
	return render(request,'contactform.html')

def Feedback(request):
	return render(request,'feedback.html')


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

	else:		
		buyerss =   Buyerinfor.objects.all()
		return render(request,'new.html',{'buyerss':buyerss})