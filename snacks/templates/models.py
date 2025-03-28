from django.db import models
import os
from django.core.files import File
from django.utils.timezone import datetime
from django.contrib.auth.models import User
from django.conf import settings
import uuid

class Client(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	client_name 	= models.CharField(max_length = 200, null = True)
	proj_name 		= models.CharField(max_length=50,null=True)
	currency_type 	= models.CharField(max_length=50,null=True)
	duration_type 	= models.CharField(max_length=50,null=True)
	price 			= models.FloatField(null=True)
	price_type 		= models.CharField(max_length=100,null=True)
	rate 		    = models.FloatField(null=True)
	tin_number 		= models.CharField(max_length=100,null=True)
	vm_name     	= models.CharField(max_length=200,null=True)
	status      	= models.IntegerField(null = True,default=0)
	change_dollar   = models.IntegerField(null = True,default=0)


class pool_master(models.Model): ## account tab
	def __unicode__(self):
		return '%s' (self.id)
	pool 	 = models.CharField(max_length=200,null=True)
	client 	 = models.ForeignKey(Client,null=True,on_delete=models.CASCADE)
	address  = models.CharField(max_length=200,null=True)
	email 	 = models.CharField(max_length=200,null=True)
	email_cc = models.CharField(max_length=200,null=True)
	vm_name  = models.CharField(max_length=200,null=True)


class Ship(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	ship_name 	= models.CharField(max_length  = 200, null = True)	
	client 	 	= models.ForeignKey(Client,null=True,on_delete=models.CASCADE)
	address  	= models.CharField(max_length=200,null=True)
	email 		= models.CharField(max_length=200,null=True)
	email_cc	= models.CharField(max_length=200,null=True)	
	vm_name     = models.CharField(max_length=200,null=True)
	vessel_type	= models.CharField(max_length = 200, null = True)
	pool_name	= models.CharField(max_length = 200, null = True)
	pool 		= models.ForeignKey(pool_master, null=True ,on_delete=models.PROTECT)

class invoice(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	invoice_no  	= models.CharField(max_length=100,null=True)
	invoice_date  	= models.DateTimeField(default=datetime.now,blank=True)
	invoice_amount  = models.FloatField(null=True)
	received_date  	= models.DateField( null = True)
	vm_name     	= models.CharField(max_length=200,null=True)
	cancel_invoice 	= models.IntegerField(null = True,default=0)
	ship_name 		= models.CharField(max_length  = 200, null = True)
	voyage_no 		= models.CharField(max_length = 200, null = True)
	proj_name  		= models.CharField(max_length=100,null=True)
	client_address	= models.CharField(max_length=200,null=True)
	payment_status 	= models.CharField(max_length=100,null=True)##paid or unpaid	
	mail_to 		= models.CharField(max_length=200,null=True)
	mail_cc 		= models.CharField(max_length=200,null=True)
	mail_from 		= models.CharField(max_length=200,null=True)
	client 	 		= models.ForeignKey(Client,null=True,on_delete=models.CASCADE)
	disch_date      = models.DateTimeField(null = True)
	disch_port      = models.CharField(max_length = 200, null = True)
	inr  			= models.CharField(max_length = 200, null = True)
	usd  			= models.CharField(max_length = 200, null = True)
	month 		 	= models.CharField(max_length=100,null=True)##paid or unpaid
	counter			= models.IntegerField(null = True,default=0)
	url      		= models.CharField(max_length=200,null=True)
	remark 		 	= models.CharField(max_length = 200, null = True)
	vessel_type	 	= models.CharField(max_length = 200, null = True)
	deadwt	 		= models.CharField(max_length = 200, null = True)
	qty 			= models.IntegerField(null = True,default=1)
	price	 		= models.FloatField(null=True)
	rate	 		= models.FloatField(null=True)
	bank_charges	= models.FloatField(null=True)
	received_inr	= models.FloatField(null=True)
	tds	   			= models.FloatField(null=True)
	rece_amount		= models.FloatField(null=True)
	month_name     	= models.CharField(max_length=100,null=True)
	price_type 		= models.CharField(max_length=100,null=True)
	account_type	= models.CharField(max_length = 200, null = True)
	total_amount	= models.FloatField(null=True)
	usd_amount		= models.FloatField(null=True)	

class Users(models.Model):
	user 			= models.OneToOneField(User, null = True)	
	user_type 		= models.CharField(max_length = 150, null = True)


class vessel_selected_invoice(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)	
	ship_name 		= models.CharField(max_length  = 200, null = True)
	voyage_no 		= models.CharField(max_length = 200, null = True)
	proj_name  		= models.CharField(max_length=100,null=True)	
	today       	= models.DateTimeField(null = True)
	voyage_cancel 	= models.IntegerField(null = True,default=0)
	disch_date      = models.DateTimeField(null = True)
	disch_port      = models.CharField(max_length = 200, null = True)
	vm_name     	= models.CharField(max_length=200,null=True)
	client 	 		= models.ForeignKey(Client,null=True,on_delete=models.CASCADE)	
	invoice_no  	= models.CharField(max_length=100,null=True)
	month 		    = models.CharField(max_length=200,null=True)
	vessel_type	 	= models.CharField(max_length = 200, null = True)	
	qty 			= models.IntegerField(null = True,default=1)	
	account_type	= models.CharField(max_length = 200, null = True)
	address  		= models.CharField(max_length=900,null=True)		

class BlueWater(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	client_name 	= models.CharField(max_length = 200, null = True)	
	tin_number 		= models.CharField(max_length=100,null=True)

class vessel_combined_invoice(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	invoice_no  	= models.CharField(max_length=100,null=True)
	voyage_no 		= models.CharField(max_length = 200, null = True)
	ship_name 		= models.CharField(max_length  = 200, null = True)	
	proj_name  		= models.CharField(max_length=100,null=True)	
	today       	= models.DateTimeField(null = True)	
	voyage_id   	= models.IntegerField(null = True,default=0)
	vm_name 		= models.CharField(max_length=200,null=True)
	client 	 		= models.ForeignKey(Client,null=True,on_delete=models.CASCADE)	
	month 		    = models.CharField(max_length=200,null=True)
	vessel_type	 	= models.CharField(max_length = 200, null = True)	
	qty 			= models.IntegerField(null = True,default=1)

class mail_invoice_details(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	invoice_no  	= models.CharField(max_length=100,null=True)	
	client 	 		= models.ForeignKey(Client,null=True,on_delete=models.CASCADE)	
	proj_name 		= models.CharField(max_length=50,null=True)
	currency_type	= models.CharField(max_length=100,null=True)

class inbox_invoice_details(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	invoice_date	= models.DateField(null = True)
	vessel_name     = models.CharField(max_length=100,null=True)
	voy_no 			= models.CharField(max_length=100,null=True)
	client 	 		= models.ForeignKey(Client,null=True,on_delete=models.CASCADE)	
	invoice_amount  = models.FloatField(null=True)
	invoice_no  	= models.CharField(max_length=100,null=True)
	pdf_path 		= models.CharField(max_length=150,null=True)	
	mail 			= models.CharField(max_length=200,null=True)
	mail_cc 		= models.CharField(max_length=200,null=True)
	mail_from 		= models.CharField(max_length=200,null=True)
	sent_mail_date  = models.DateField(null = True)

class new_users(models.Model):
	user 			 = models.ForeignKey(User,null=True)
	change_password  = models.CharField(max_length = 150, null = True)	
	changed_pwd_date = models.DateTimeField(auto_now_add=True)


class delete_vessel_details(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	invoice_date   = models.DateField(null = True)
	delete_date    = models.DateTimeField(default=datetime.now,blank=True)	
	ship_name 	   = models.CharField(max_length=100,null=True)
	voy_no 		   = models.CharField(max_length=100,null=True)
	invoice_no     = models.CharField(max_length=100,null=True)	
	client_id 	   = models.ForeignKey(Client,null=True,on_delete=models.CASCADE)	
	proj_name 	   = models.CharField(max_length=50,null=True)
	currency_type  = models.CharField(max_length=50,null=True)	
	price 		   = models.FloatField(null=True)
	remarks        = models.CharField(max_length=100,null=True)


class price_type_details(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	price_type     = models.CharField(max_length=50,null=True)

class cost_per_route(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	cost  			= models.FloatField(null=True)
	route 			= models.CharField(max_length=50,null=True)	
	client_id 	    = models.ForeignKey(Client,null=True,on_delete=models.CASCADE)	

class generate_invoice(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)	
	invoice_no 		= models.CharField(max_length=350,null=True)	
	currency_type 	= models.CharField(max_length=50,null=True)	

	
class generate_for_vessel(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)	
	ship_name		= models.CharField(max_length=50,null=True)	
	voyage_no		= models.CharField(max_length=50,null=True)
	client_id 	    = models.ForeignKey(Client,null=True,on_delete=models.CASCADE)
	currency_type 	= models.CharField(max_length=50,null=True)
	discharge_port	= models.CharField(max_length=50,null=True)	

class copy_data(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)	
	ship_name		= models.CharField(max_length=150,null=True)	
	voyage_no		= models.CharField(max_length=150,null=True)
	client_id 	    = models.ForeignKey(Client,null=True,on_delete=models.CASCADE)
	currency_type 	= models.CharField(max_length=150,null=True)	
	pic				= models.CharField(max_length=150,null=True)	
	disch_date		= models.DateTimeField(null = True)
	client_name		= models.CharField(max_length=250,null=True)	
	invoice_amount 	= models.CharField(max_length=100,null=True)
	received_date	= models.CharField(max_length=50,null=True)
	invoice_no		= models.CharField(max_length=150,null=True)	
	invoice_date 	= models.DateTimeField(null = True)
	disch_port		= models.CharField(max_length=150,null=True)	
	price_type		= models.CharField(max_length=150,null=True)
	paid 			= models.CharField(max_length=150,null=True)

def get_file_path(instance, filename):
	try:
		os.remove('/var/www/html/invoice/it/static/excel/'+str(filename))
	except:
	 	pass
	return os.path.join('/var/www/html/invoice/it/static/excel/'+str(filename))

class uploader(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)	
	invoice_excel	= models.FileField(upload_to=get_file_path,null=True)	
	upload_date 	= models.DateField( null = True)
	file_name		= models.CharField(max_length=150,null=True)	


class copy_data_boss(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)	
	client_name		= models.CharField(max_length=150,null=True)	
	invoice_no		= models.CharField(max_length=150,null=True)	
	received_date 	= models.DateField(null = True)
	amount 			= models.CharField(max_length=100,null=True)

class json_data(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)	
	upload_date 	= models.DateField(null = True)
	file_name       = models.CharField(max_length=100,null=True)
	#path_name       = models.CharField(max_length=100,null=True)

class api_client_data(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)	
	ship_id		= models.CharField(max_length=150,null=True)	
	account_tab	= models.CharField(max_length=150,null=True)	
	client_id 	= models.CharField(max_length=150,null=True)	
	ship_name 	= models.CharField(max_length=100,null=True)