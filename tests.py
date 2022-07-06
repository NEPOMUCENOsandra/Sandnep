from django.test import TestCase
from soapsystem.views import MainPage
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.urls import resolve
from .models import form


class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')

	def test_save_post_request(self):
		response = self.client.post('/', {'name': 'Sandra Nepomuceno',
		 'add' : 'Villa Vieja Subdivision Georgetown Heights',
		 'email' : 'sandra.nepomuceno@gsfe.tupcavite.edu.ph',
		 'contact' : '09123456789'})

		self.assertEqual(form.objects.count(),1)
		
		checkData = form.objects.first()
		self.assertEqual(checkData.newfirstname, 'Sandra Nepomuceno')
		self.assertEqual(checkData.newaddress, 'Villa Vieja Subdivision Georgetown Heights')
		self.assertEqual(checkData.newemail, 'sandra.nepomuceno@gsfe.tupcavite.edu.ph')
		self.assertEqual(checkData.newcontact, '09123456789')


	def test_model_data(self):
		self.client.get('/')
		self.assertEqual(form.objects.count(), 0)

class ORMtest(TestCase):
	def test_retreived(self):

#firstinput		
		modelscontainer = form()
		modelscontainer.newfirstname = 'Sandra Nepomuceno'
		modelscontainer.newaddress = 'Villa Vieja Subdivision Georgetown Heights'
		modelscontainer.newemail = 'sandra.nepomuceno@gsfe.tupcavite.edu.ph'
		modelscontainer.newcontact = '09123456789'
		modelscontainer.save()

#secondinput

		modelscontainer2 = form()
		modelscontainer2.newfirstname = 'Anne Lorie'
		modelscontainer2.newaddress = 'Emerald St. Queen City'
		modelscontainer2.newemail = 'Emy@gmail.com'
		modelscontainer2.newcontact = '09093874509'
		modelscontainer2.save()

		formlist = form.objects.all()
		self.assertEqual(formlist.count(), 2)

		input1 = formlist[0]
		input2 = formlist[1]

		self.assertEqual(input1.newfirstname, 'Sandra Nepomuceno')
		self.assertEqual(input1.newaddress, 'Villa Vieja Subdivision Georgetown Heights')
		self.assertEqual(input1.newemail, 'sandra.nepomuceno@gsfe.tupcavite.edu.ph')
		self.assertEqual(input1.newcontact, '09123456789')

		self.assertEqual(input2.newfirstname, 'Anne Lorie')
		self.assertEqual(input2.newaddress, 'Emerald St. Queen City')
		self.assertEqual(input2.newemail, 'Emy@gmail.com')
		self.assertEqual(input2.newcontact, '09093874509')

	def test_testing_template(self):
		form.objects.create(newfirstname = 'Sandra Nepomuceno', 
			newaddress = 'Villa Vieja Subdivision Georgetown Heights', 
			newemail = 'sandra.nepomuceno@gsfe.tupcavite.edu.ph', 
			newcontact = '09123456789')

		form.objects.create(newfirstname = 'Anne Lorie', 
			newaddress = 'Emerald St. Queen City', 
			newemail = 'Emy@gmail.com', 
			newcontact = '09093874509')

		response = self.client.get('/')
		self.assertIn('1: Sandra Nepomuceno Villa Vieja Subdivision Georgetown Heights sandra.nepomuceno@gsfe.tupcavite.edu.ph 09123456789', response.content.decode())
		self.assertIn('2: Anne Lorie Emerald St. Queen City Emy@gmail.com 09093874509', response.content.decode())