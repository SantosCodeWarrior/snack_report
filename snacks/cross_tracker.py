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


def cross_tracker(request):
	journal_master  = models.journal_master.objects.all()
	tiffin_master   = models.tiffin_master.objects.all()
	date_filter_det = models.journal_master.objects.all().order_by('entry_date')
	
	dat_array       = []
	snack_details 	= []
	for c in date_filter_det:
		if c.entry_date not in dat_array:
			dat_array.append(c.entry_date)

	rate_dinner = 0
	rate_lunch  = 0
	rate_break  = 0
	sums 		= 0.0
	
	get_tiffin_details 	= models.tiffin_master.objects.all()
	fixed_rate         	= models.fixed_rate_master.objects.all()
	all_array 			= len(date_filter_det)	
	r=0
	for w in range(0,all_array):		
		for t in dat_array:
			try:
				i  = models.journal_master.objects.filter(entry_date=t)			
				if i[w].tiffin_breakfast_qty!=0:
					rate_breakfast 	= get_tiffin_details[0].rate
				elif i[w].tiffin_lunch_qty!=0:
					rate_lunch 		= get_tiffin_details[1].rate
				elif i[w].tiffin_dinner_qty!=0:
					rate_dinner 	= get_tiffin_details[2].rate
				else:
					rate_breakfast = 0.0
					rate_lunch     = 0.0
					rate_dinner    = 0.0	
				
				sums  		= (i[w].amount+i[w].tiffin_total)
				static_rate = fixed_rate[0].rate
				if i[w].tiffin_total<=static_rate:				
					overdue = 0
				else:
					overdue = (i[w].amount-i[w].tiffin_total)	

				snack_details.append({
					's_no'			: r,					
					'staff_name' 	: i[w].staff.staff_master,
					'entry_date' 	: t,
					'snack_amt'    	: i[w].amount,
					'tiffin_amt' 	: i[w].tiffin_total,
					'breakfast'  	: rate_breakfast,
					'lunch' 		: rate_lunch,
					'dinner'		: rate_dinner,
					'overdue'       : overdue,
					'snack_tiffin'  : sums,
					})				
			except:
				pass
			r+=1
	
	snack_details.sort(reverse=True)
	context={
		'journal_master' : journal_master,
		'tiffin_master'	 : tiffin_master,
		'dat_array' 	 : dat_array,
		'snack_details'  : snack_details,

	}
	return render_to_response("tracker/cross_tracker.html",context)
