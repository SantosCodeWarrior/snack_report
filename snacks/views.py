from django.shortcuts import render
from django.shortcuts import render,render_to_response
from snacks import models
from django.http import HttpResponse
import json
from django.db.models import Count
from datetime import date,timedelta,datetime
from collections import Counter
import numpy as np
import decimal
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import os
import time
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import requests
from num2words import num2words

#####################################################
import smtplib
from django.core.mail.message import EmailMessage
from django.core.mail import send_mail
from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import os,sys
from os import path
import re
import sys, ast
import subprocess
from subprocess import Popen, PIPE
import pprint
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import requests
import re
from bs4 import BeautifulSoup
from decimal import Decimal
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import pdfkit
import webbrowser
from django.db.models import Max
from django.db.models import Min
from shutil import copyfile
import shutil
from django.db.models import Sum
from time import strptime
from calendar import monthrange
from django.db import connection
import smbclient 
import os 
from shutil import copyfile    
import shutil
from smb import smb_structs
from smb.SMBConnection import SMBConnection
from nmb.NetBIOS import NetBIOS
smb_structs.SUPPORT_SMB2 = True
import urllib
import tempfile
import urllib2
from smb.SMBHandler import SMBHandler


def dashboard(request):		
	return render_to_response("base.html",{})

def master_entry(request):
	staff_list = models.master_register.objects.all().order_by('staff_master')
	context={
		'staff_list' : staff_list
	}
	return render_to_response("entry_data/master_entry.html",context)

def submit_staff_master(request):
	staff_name 	= request.GET['staff_name']
	email 		= request.GET['email']	
	check 		= models.master_register.objects.filter(staff_master=staff_name).count()	
	if check!=0:
		db 	= models.master_register.objects.filter(staff_master=staff_name).first()
		msg = 'already'
	else:
		db 	= models.master_register()
		msg = 'done'

	db.staff_master = staff_name
	db.email 		= email
	db.save()

	return HttpResponse(json.dumps(msg))

def update_staff_master(request):
	staff_name 			= request.GET['e_staff_name']
	email 				= request.GET['e_mail']
	ids 				= request.GET['e_id']
	upDB 				= models.master_register.objects.filter(id=ids).first()
	upDB.staff_master 	= staff_name
	upDB.email 			= email
	upDB.save()
	return HttpResponse(json.dumps('done'))


def snacks_entry(request):	
	items_list = models.standard_snacks_list.objects.all().order_by('items')
	context={
		'items_list' : items_list
	}	
	return render_to_response("entry_data/snack_entry.html",context)

def submit_snack_list(request):
	items 	= request.GET['items']
	rate 	= request.GET['rate']	
	check 	= models.standard_snacks_list.objects.filter(items=items).count()	
	if check!=0:
		db 	= models.standard_snacks_list.objects.filter(items=items).first()
		msg = 'already'
	else:
		db 	= models.standard_snacks_list()
		msg = 'done'

	db.items = items
	db.rate  = rate
	db.save()
	return HttpResponse(json.dumps(msg))

def update_snacks_items(request):
	items 	    = request.GET['e_items']
	rate 		= request.GET['e_rates']
	ids 		= request.GET['e_id']
	upDB 		= models.standard_snacks_list.objects.filter(id=ids).first()
	upDB.items 	= items
	upDB.rate 	= rate
	upDB.save()
	return HttpResponse(json.dumps('done'))

def journal_entry(request):
	
	return render_to_response("entry_data/journal_entry.html")

def get_staff_data(request):
	staff_data	= models.master_register.objects.all().order_by('staff_master')	
	staff_array = []
	for c in staff_data:
		staff_array.append({
			'staff_name' :  c.staff_master,
			})

	items_data	= models.standard_snacks_list.objects.all().order_by('items')	
	items_array = []
	for c in items_data:
		items_array.append({
			'items' : c.items,
			'rate'  : c.rate,
			})

	context={
		'staff_array' : staff_array,
		'items_array' : items_array
	}

	return HttpResponse(json.dumps(context))

def get_rate_data(request):
	try:
		valueAtC 		= request.GET['item_name']
		get_items_name	= models.standard_snacks_list.objects.filter(items=valueAtC).first()
		if get_items_name:
			get_rate = get_items_name.rate
		else:
			get_rate = ""
	except:
		pass
	#print '----',get_rate,'----',valueAtC
	return HttpResponse(json.dumps(get_rate))

def get_total_tiffin(request):	
	tiffin = []
	get_tiffin	= models.tiffin_master.objects.all()
	for x in get_tiffin:
		tiffin.append({
			'tiffin_type' : x.tiffin_type,
			'tiffin_rate' : x.rate
			})
	return HttpResponse(json.dumps(tiffin))


def get_amount_details(request):
	try:
		items = request.GET['items']
		qty   = request.GET['qty']
		get_items_name	= models.standard_snacks_list.objects.filter(items=items).first()
		if get_items_name:
			get_amount = float(get_items_name.rate)*float(qty)
		else:
			get_amount = 1
	except:
	 	get_amount = ''
	return HttpResponse(json.dumps(get_amount))


@csrf_exempt
def submit_journal_data(request):
	journal_data  	= json.loads(request.POST['journal_data'])
	amt 			= 0.0	
	get_array 		= []
	calc_array 		= []
	
	today			= datetime.now().date() 	
	for c in journal_data:
		sums 		= 0		
		if c[1]!=None or c[2]!=None or c[3]!=None or c[4]!=None or c[5]!=None or c[7]!=None  or c[9]!=None or c[0]!=None: 
			id_s 				 = c[0]
			entry_date 			 = c[1]
			staff_name 			 = c[2]			
						
			tiffin_breakfast_qty = str(c[3])
			tiffin_lunch_qty     = str(c[4])
			tiffin_dinner_qty 	 = str(c[5])
			standard_items 		 = c[7]			
			qty 				 = c[9]			
			get_snack_id		 = models.standard_snacks_list.objects.filter(items=standard_items).first()
			get_staff_id 		 = models.master_register.objects.filter(staff_master=staff_name).first()
			get_tiffin_details	 = models.tiffin_master.objects.all()			
			
			if tiffin_breakfast_qty=="1" and tiffin_lunch_qty=="1" and tiffin_dinner_qty=="1":
				calc_array 	= [get_tiffin_details[0].rate,get_tiffin_details[1].rate,get_tiffin_details[2].rate]				
			if tiffin_breakfast_qty=="1" and tiffin_lunch_qty!="1" and tiffin_dinner_qty=="1":
				calc_array 	= [get_tiffin_details[0].rate,0,get_tiffin_details[2].rate]				
			if tiffin_breakfast_qty=="1" and tiffin_lunch_qty!="1" and tiffin_dinner_qty!="1":
				calc_array 	= [get_tiffin_details[0].rate,0,0]				
			if tiffin_breakfast_qty!="1" and tiffin_lunch_qty=="1" and tiffin_dinner_qty=="1":
				calc_array 	= [0,get_tiffin_details[1].rate,get_tiffin_details[2].rate]				
			if tiffin_breakfast_qty!="1" and tiffin_lunch_qty=="1" and tiffin_dinner_qty!="1":
				calc_array 	= [0,get_tiffin_details[1].rate,0]				
			if tiffin_breakfast_qty!="1" and tiffin_lunch_qty!="1" and tiffin_dinner_qty=="1":
				calc_array 	= [0,0,get_tiffin_details[2].rate]				
			if tiffin_breakfast_qty=="1" and tiffin_lunch_qty=="1" and tiffin_dinner_qty!="1":
				calc_array 	= [get_tiffin_details[0].rate,get_tiffin_details[1].rate,0]				
			if tiffin_breakfast_qty!="1" and tiffin_lunch_qty!="1" and tiffin_dinner_qty!="1":
				calc_array 	= [0,0,0]

			for i in calc_array:
				sums = sums + i
			total_tiffin = sums	
			
			if id_s:
				db = models.journal_master.objects.filter(id=id_s).first()				
			else:
				db = models.journal_master()				

			try:
				breakx = int(tiffin_breakfast_qty)
			except:
				breakx = 0

			try:
				lunchx = int(tiffin_lunch_qty)
			except:
				lunchx = 0

			try:
				dinnerx = int(tiffin_dinner_qty)
			except:
				dinnerx = 0			

			try:
				rate = get_snack_id.rate
			except:
				rate = 0.0
			try:
				amt  = float(rate)*float(qty)
			except:
				amt  = 0.0
			#try:
			db.entry_date  	 		= str(entry_date)
			db.staff_id    			= get_staff_id.id
			db.standard_id 			= get_snack_id.id
			db.tiffin_breakfast_qty = (tiffin_breakfast_qty)
			db.tiffin_lunch_qty 	= (tiffin_lunch_qty)
			db.tiffin_dinner_qty    = (tiffin_dinner_qty)
			db.tiffin_total         = total_tiffin
			db.qty                  = qty
			db.amount 				= amt	
			db.save()
			#except:
			#	pass				

			
	return HttpResponse(json.dumps('done'))

@csrf_exempt
def get_tab_name(request):
	tabs 	= models.journal_master.objects.all()
	tab_l 	= []
	s_no = 1
	for r in tabs:
		
		if r.staff_id:
			staff_name = r.staff.staff_master
		else:
			staff_name = ""	

		if r.standard_id:
			items = r.standard.items
		else:
			items = ""

		tab_l.append({
			"id"				: r.id,
			"name"				: staff_name,
			"staff_name" 		: staff_name,
			"standard_items" 	: items,
			"standard_qty"		: r.qty,
			"qty_breakfast"  	: r.tiffin_breakfast_qty,
			"qty_lunch"  		: r.tiffin_lunch_qty,
			"qty_dinner" 		: r.tiffin_dinner_qty,
			"total_tifin"		: r.tiffin_total,
			"snack_amt"			: r.amount,	
			"standard_rate"     : r.standard.rate,
			"date"				: str(r.entry_date),
			"userID"			: s_no
		})
		s_no+=1	
		print '-------',tab_l

	return HttpResponse(json.dumps(tab_l))		

def tiffin_entry(request):
	tiffin_list = models.tiffin_master.objects.all().order_by('tiffin_type')
	context={
		'tiffin_list' : tiffin_list
	}
	return render_to_response("entry_data/tiffin_entry.html",context)


def submit_tiffin_list(request):
	items 	= request.GET['items']
	rate 	= request.GET['rate']	
	check 	= models.tiffin_master.objects.filter(tiffin_type=items).count()	
	if check!=0:
		db 	= models.tiffin_master.objects.filter(tiffin_type=items).first()
		msg = 'already'
	else:
		db 	= models.tiffin_master()
		msg = 'done'

	db.tiffin_type 	= items
	db.rate  		= rate
	db.save()
	return HttpResponse(json.dumps(msg))

def update_tiffin_items(request):
	items 	    		= request.GET['e_items']
	rate 				= request.GET['e_rates']
	ids 				= request.GET['e_id']
	upDB 				= models.tiffin_master.objects.filter(id=ids).first()
	upDB.tiffin_type 	= items
	upDB.rate 			= rate
	upDB.save()
	return HttpResponse(json.dumps('done'))


def owner_list(request):
	owner_list = models.owner_master.objects.all().order_by('owner_name')
	context={
		'owner_list' : owner_list
	}
	return render_to_response("entry_data/owner_list.html",context)

def submit_owner_list(request):
	owner_name		= request.GET['owner_name']
	contact_no		= request.GET['contact_no']
	email_id		= request.GET['email_id']
	shop_name		= request.GET['shop_name']
	address			= request.GET['address']
	check 	= models.owner_master.objects.filter(owner_name=owner_name).count()	
	if check!=0:
		db 	= models.owner_master.objects.filter(owner_name=owner_name).first()
		msg = 'already'
	else:
		db 	= models.owner_master()
		msg = 'done'

	db.owner_name 	= owner_name
	db.address 		= address
	db.email 		= email_id
	db.contact_no 	= contact_no
	db.shop_name 	= shop_name
	db.save()
	return HttpResponse(json.dumps(msg))

def update_owner_data(request):
	e_id 		 	= request.GET['e_id']
	e_owner_name 	= request.GET['e_owner_name']
	e_contact_no 	= request.GET['e_contact_no']
	e_email_id 		= request.GET['e_email_id']
	e_shop_name 	= request.GET['e_shop_name']
	e_address 		= request.GET['e_address']	

	upDB 			= models.owner_master.objects.filter(id=e_id).first()
	upDB.owner_name = e_owner_name
	upDB.address 	= e_address
	upDB.email 		= e_email_id
	upDB.contact_no = e_contact_no
	upDB.shop_name 	= e_shop_name
	upDB.save()
	return HttpResponse(json.dumps('done'))
