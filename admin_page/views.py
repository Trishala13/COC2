from __future__ import unicode_literals
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
import MySQLdb

def view_zone(request):
	db=MySQLdb.connect(user="root",host="localhost",passwd="12345",db="COC")
	cursor=db.cursor()
	cursor.execute("""Select * from zone""")
	result=cursor.fetchall()
	return render(request, 'admin_page/view_zone.html', {'zone_list':result})

def view_division(request):
	db=MySQLdb.connect(user="root",host="localhost",passwd="12345",db="COC")
	cursor=db.cursor()
	cursor.execute("""Select * from division""")
	result=cursor.fetchall()
	return render(request, 'admin_page/view_division.html', {'division_list':result})

def view_user(request):
	db=MySQLdb.connect(user="root",host="localhost",passwd="12345",db="COC")
	cursor=db.cursor()
	cursor.execute("""Select * from user""")
	result=cursor.fetchall()
	user=[]
	for x in result:
		y=list(x)
		user.append(y.remove(y[-1]))
	result=user
	return render(request, 'admin_page/view_user.html', {'user_list':result})

def view_employee(request):
	db=MySQLdb.connect(user="root",host="localhost",passwd="12345",db="COC")
	cursor=db.cursor()
	cursor.execute("""Select * from employee""")
	result=cursor.fetchall()
	user=[]
	for x in result:
		y=list(x)
		user.append(y.remove(y[-1]))
	return render(request, 'admin_page/view_employee.html', {'employee_list':user})

def view_complaint(request):
	db=MySQLdb.connect(user="root",host="localhost",passwd="12345",db="COC")
	cursor=db.cursor()
	cursor.execute("""Select * from complaint""")
	result=cursor.fetchall()
	return render(request, 'admin_page/view_complaint.html' , {'complaint_list':result})

def view_feedback(request):
	db=MySQLdb.connect(user="root",host="localhost",passwd="12345",db="COC")
	cursor=db.cursor()
	cursor.execute("""Select * from feedback""")
	result=cursor.fetchall()
	return render(request, 'admin_page/view_feedback.html', {'feedback_list':result})

def view_news(request):
	db=MySQLdb.connect(user="root",host="localhost",passwd="12345",db="COC")
	cursor=db.cursor()
	cursor.execute("""Select * from news""")
	result=cursor.fetchall()
	return render(request, 'admin_page/view_news.html', {'news_list':result})

def employee(request):
	return render(request,'admin_page/employee.html',{})

def user(request):
	return render(request,'admin_page/user.html',{})

def zone(request):
	return render(request,'admin_page/zone.html',{})

def division(request):
	return render(request,'admin_page/division.html',{})

def news(request):
	return render(request,'admin_page/news.html',{})

def add_zone(request):
	zone_id=request.GET.get("zone",None)
	name=request.GET.get("zname",None)
	area=request.GET.get("area",None)
	return render(request,'admin_page/zone.html',{})

def add_division(request):
	div_id=request.GET.get("division",None)
	name=request.GET.get("dname",None)
	n_can=request.GET.get("can",None)
	num=request.GET.get("num",None)
	zone=request.GET.get("zone",None)
	return render(request,'admin_page/division.html',{})

def add_employee(request):
	emp_id=request.GET.get("id",None)
	name=request.GET.get("name",None)
	aadhar=request.GET.get("aadhar",None)
	designation=request.GET.get("designation", None)      
	clas=request.GET.get("class",None)
	phone=request.GET.get("phone",None)
	address=request.GET.get("address",None)
     	zone=request.GET.get("zone",None)
	division=request.GET.get("division",None)
	return render(request,'admin_page/employee.html',{})

def add_news(request):
	return render(request,'admin_page/news.html',{})

def delete_employee(request):
	emp_id=request.GET.get("emp_id",None)
	return render(request,'admin_page/employee.html',{})

def update_employee(request):	
	emp_id=request.GET.get("emp_id",None)
	designation=request.GET.get("designation", None)      
	clas=request.GET.get("class",None)
	phone=request.GET.get("phone",None)
	address=request.GET.get("address",None)
     	zone=request.GET.get("zone",None)
	division=request.GET.get("division",None)
	request["emp_id"]=""
	return render(request,'admin_page/employee.html',{})

def update_zone(request):
	z_id=request.GET.get("z_id",None)
	area=request.GET.get("area",None)	
	pop=request.GET.get("pop",None)
	request["zoneid"]=""
	return render(request,'admin_page/zone.html',{})

def update_division(request):
	d_id=request.GET.get("d_id",None)
	n_can=request.GET.get("can",None)
	num=request.GET.get("num",None)
	return render(request,'admin_page/division.html',{})

def delete_news(request):
	news_id=request.GET.get("id",None)
	return render(request,'admin_page/news.html',{})
	
