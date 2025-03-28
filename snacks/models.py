from django.db import models
import os
from django.core.files import File
from django.utils.timezone import datetime
from django.contrib.auth.models import User
from django.conf import settings
import uuid

class master_register(models.Model):
	def __unicode__(self):
		return '%s' (self.id)
	staff_master 			= models.CharField(max_length=200,null=True)	
	email 	 				= models.CharField(max_length=200,null=True)	
	

class standard_snacks_list(models.Model):
	def __unicode__(self):
		return '%s' (self.id)
	items 					= models.CharField(max_length=200,null=True)	
	rate 					= models.FloatField(null=True)


class expense_master(models.Model):
	def __unicode__(self):
		return '%s' (self.id)
	items_type 				= models.CharField(max_length=200,null=True)	
	

class billing(models.Model):
	def __unicode__(self):
		return '%s' (self.id)
	bill_type 				= models.CharField(max_length=200,null=True)	
	
class vendor_master(models.Model):
	def __unicode__(self):
		return '%s' (self.id)
	vendor_name 			= models.CharField(max_length=200,null=True)
	address  				= models.CharField(max_length=200,null=True)
	email 	 				= models.CharField(max_length=200,null=True)	
	contact_no 	 			= models.CharField(max_length=200,null=True)	
	

class tiffin_master(models.Model):
	def __unicode__(self):
		return '%s' (self.id)
	tiffin_type 			= models.CharField(max_length=200,null=True)
	rate 					= models.FloatField(null=True)	


class owner_master(models.Model):
	def __unicode__(self):
		return '%s' (self.id)
	owner_name 				= models.CharField(max_length=200,null=True)
	address  				= models.CharField(max_length=200,null=True)
	email 	 				= models.CharField(max_length=200,null=True)	
	contact_no 	 			= models.CharField(max_length=200,null=True)	
	shop_name   			= models.CharField(max_length=200,null=True)
	status 					= models.IntegerField(null = True,default=0)
	

class journal_master(models.Model):
	def __unicode__(self):
		return '%s' (self.id)
	staff 					= models.ForeignKey(master_register, null=True ,on_delete=models.PROTECT)	
	entry_date  			= models.DateField( null = True)
	tiffin_breakfast_qty 	= models.IntegerField(null = True,default=0)
	tiffin_lunch_qty 		= models.IntegerField(null = True,default=0)
	tiffin_dinner_qty 		= models.IntegerField(null = True,default=0)
	tiffin_total 			= models.FloatField(null=True)
	standard				= models.ForeignKey(standard_snacks_list, null=True ,on_delete=models.PROTECT)
	qty 					= models.IntegerField(null = True,default=0)
	amount 					= models.FloatField(null=True)
	
class fixed_rate_master(models.Model):
	def __unicode__(self):
		return '%s' (self.id)	
	rate 					= models.FloatField(null=True)	
