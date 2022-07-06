from django.db import models

class Topay(models.Model):
	street= models.CharField(max_length=200)
	subd= models.CharField(max_length=200)
	brgy= models.CharField(max_length=200)
	city= models.CharField(max_length=200)
	zipcode= models.IntegerField()
class meta:
		db_table = "Topay"


class Buyerinfor(models.Model):
	lastname = models.CharField(max_length=300)	
	firstname = models.CharField(max_length=300)
	middlename = models.CharField(max_length=300)
	contact = models.IntegerField()
	email = models.EmailField(max_length=254, default="", blank=True, null=True)
class meta:
		db_table = "Buyerinfor"


class SoapBuy(models.Model):
	soapname = models.CharField(max_length=300)	
	qty = models.CharField(max_length=300)
class meta:
	db_table = "SoapBuy"


class Feedback(models.Model):
	rate= models.CharField(max_length=200)
	message= models.TextField(max_length=200)


class ContactForm(models.Model):
	email= models.CharField(max_length=200)
	message= models.TextField(max_length=200)
