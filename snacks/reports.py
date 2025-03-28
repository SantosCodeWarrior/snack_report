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


def reports(request):
	owner_list = models.owner_master.objects.filter(status=0).order_by('owner_name')
	context={
		'owner_list' : owner_list
	}
	return render_to_response("report/reports.html",context)

def get_owner_master(request):
	owner_list 		= request.GET['owner_list']
	get_owner_list 	= models.owner_master.objects.filter(id=owner_list).first()
	get_info 		= []
	get_info.append({
		'address' 		: get_owner_list.address,
		'contact_no' 	: get_owner_list.contact_no,
		'owner_name' 	: get_owner_list.owner_name,
		})
	context={
		'get_info' : get_info
	}
	return HttpResponse(json.dumps(context))


@csrf_exempt
def get_reports_data(request):
	date_filter = request.POST['date_filter']	
	tabs 		= models.journal_master.objects.filter(entry_date=date_filter)	
	
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
			"id"			: r.id,			
			"staff_name"	: staff_name,
			"items" 		: items,
			"qty"			: r.qty,			
			"amount"		: r.amount,	
			"rate"     		: r.standard.rate,
			"date"			: str(r.entry_date),
			"id"			: s_no
		})
		s_no+=1	
	return HttpResponse(json.dumps(tab_l))