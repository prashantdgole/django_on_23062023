# my_tennis_club\my_tennis_club\members\

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Member
from .models import Voucher
from .models import Post
from .models import Blog
from django.urls import reverse
from my_tennis_club.settings import ROOT_EDITDELETE


def mshow(request):
      mymembers = Member.objects.all().values()  
      template = loader.get_template( 'all_members.html')
      context = { 'mymembers': mymembers, }
      return HttpResponse(template.render(context, request))
 

def madd(request):
  template = loader.get_template('madd.html')
  return HttpResponse(template.render({}, request))

def medit(request):
  ROOT_EDITDELETE=1
  #mymember =  ROOT_EDITDELETE
  myeditdelete =  ROOT_EDITDELETE
  mymembers = Member.objects.all().values()  
  template = loader.get_template('medit.html')
  context = {  'myeditdelete': ROOT_EDITDELETE,
                       'mymembers': mymembers, 
                   }
  #context = {"editdelete": ROOT_EDITDELETE,}
  #return HttpResponse(template.render({}, request))
  return HttpResponse(template.render(context, request))


def mdelete(request):
  ROOT_EDITDELETE=0
  #mymember =  ROOT_EDITDELETE
  myeditdelete =  ROOT_EDITDELETE
  mymembers = Member.objects.all().values()  
  template = loader.get_template('medit.html')
  context = {  'myeditdelete': ROOT_EDITDELETE,
                       'mymembers': mymembers, 
                   }
  #context = {"editdelete": ROOT_EDITDELETE,}
  #return HttpResponse(template.render({}, request))
  return HttpResponse(template.render(context, request))

def membeditdetails(request, id):  # new
  mymember = Member.objects.get(id=id)
  template = loader.get_template('membeditdetails.html')
  context = {  'mymember': mymember, }
  return HttpResponse(template.render(context, request))

def membdeletedetails(request, id):  # new
  mymember = Member.objects.get(id=id)
  template = loader.get_template('membdeletedetails.html')
  context = {  'mymember': mymember, }
  return HttpResponse(template.render(context, request))

def editrecord(request,id):
  x = request.POST['first']
  y = request.POST['last']
  jdt = request.POST['jdate']
  pho = request.POST['phone']
  fb = request.POST['feesbalance']
  fp = request.POST['feespaid']
  fpd = request.POST['feespaiddate']
  member = Member.objects.get(id=id)
  member.firstname=x
  member.lastname=y
  member.joined_date=jdt
  member.phone=pho
  member.fees_balance=fb
  member.fees_paid=fp
  member.fees_paid_date=fpd
  member.save()
  return HttpResponseRedirect(reverse('mshow'))

def deleterecord(request,id):
  member = Member.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('mshow'))

  

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  jdt = request.POST['jdate']
  pho = request.POST['phone']
  fb = request.POST['feesbalance']
  fp = request.POST['feespaid']
  fpd = request.POST['feespaiddate']
  member = Member(firstname=x, lastname=y,joined_date=jdt,phone=pho,fees_balance=fb,fees_paid=fp,fees_paid_date=fpd)
  member.save()
  return HttpResponseRedirect(reverse('mshow'))

def blogs(request):
     myblog= Blog.objects.all().values()
     template=loader.get_template('all_blogs.html')
     context={'myblog':myblog,}
     return HttpResponse(template.render(context, request))


def posts(request):
     mypost= Post.objects.all().values()
     template=loader.get_template('all_posts.html')
     context={'mypost':mypost,}
     return HttpResponse(template.render(context, request))
 
def membersmain(request):
  template = loader.get_template('membersmain.html')
  return HttpResponse(template.render())
 
def members(request):
      mymembers = Member.objects.all().values()
      template = loader.get_template('membersmain.html') 
 #    template = loader.get_template( 'all_members.html')
      context = { 'mymembers': mymembers, }
      return HttpResponse(template.render(context, request))

def details(request, id):  # new
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {  'mymember': mymember, }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def vouchersmain(request):
  template = loader.get_template('vouchersmain.html')
  return HttpResponse(template.render())

def vouchers(request):
  myvouchers=Voucher.objects.all().values()
  template = loader.get_template('vouchers.html')
  context={'myvouchers':myvouchers,}
  return HttpResponse(template.render(context,request))


def vadd(request):
  template = loader.get_template('vadd.html')
  return HttpResponse(template.render({}, request))

def voucheraddrecord(request):
  vdt = request.POST['vvoucher_date']
  vam = request.POST['vvoucher_amount']
  vpd = request.POST['vpaid_to']
  vdc = request.POST['vdebitcredit']
  vbc = request.POST['vbankorcash']
  vn1 = request.POST['vnarration1']
  vn2 = request.POST['vnarration2']
  voucher = Voucher(voucherdate=vdt, voucheramount=vam,paid_to=vpd,debitcredit=vdc,bankorcash=vbc,narration1=vn1,narration2=vn2)
  voucher.save()
  return HttpResponseRedirect(reverse('vouchers'))

def vedit(request):
  ROOT_VEDITDELETE=1
  myveditdelete =  ROOT_VEDITDELETE
  myvoucher = Voucher.objects.all().values()  
  template = loader.get_template('vedit.html')
  context = {  'myveditdelete': ROOT_VEDITDELETE,
                       'myvoucher': myvoucher, 
                   }
  return HttpResponse(template.render(context, request))

def vdelete(request):
  ROOT_VEDITDELETE=0
  myveditdelete =  ROOT_VEDITDELETE
  myvoucher = Voucher.objects.all().values()  
  template = loader.get_template('vedit.html')
  context = {  'myveditdelete': ROOT_VEDITDELETE,
                       'myvoucher': myvoucher, 
                   }
  return HttpResponse(template.render(context, request))


def vouchereditdetails(request, id):  # new
  myvoucher= Voucher.objects.get(id=id)
  template = loader.get_template('vouchereditdetails.html')
  context = {  'myvoucher': myvoucher, }
  return HttpResponse(template.render(context, request))

def voucherdeletedetails(request, id):  # new
  myvoucher = Voucher.objects.get(id=id)
  template = loader.get_template('voucherdeletedetails.html')
  context = {  'myvoucher': myvoucher, }
  return HttpResponse(template.render(context, request))

def voucherdeleterecord(request,id):
  voucher = Voucher.objects.get(id=id)
  voucher.delete()
  return HttpResponseRedirect(reverse('vouchers'))

  

def vouchereditrecord(request,id):
  vdt = request.POST['vvoucher_date']
  vam = request.POST['vvoucher_amount']
  vpd = request.POST['vpaid_to']
  vdc = request.POST['vdebitcredit']
  vbc = request.POST['vbankorcash']
  vn1 = request.POST['vnarration1']
  vn2 = request.POST['vnarration2']
  myvoucher = Voucher.objects.get(id=id)  
  myvoucher.voucherdate=vdt
  myvoucher.voucheramount=vam
  myvoucher.paid_to=vpd
  myvoucher.debitcredit=vdc
  myvoucher.bankorcash=vbc
  myvoucher.narration1=vn1
  myvoucher.narration2=vn2
  myvoucher.save()
  return HttpResponseRedirect(reverse('vouchers'))


def testing(request):
  template = loader.get_template('template.html')
  context = {    'fruits': ['Apple', 'Banana', 'Cherry'],     }
  return HttpResponse(template.render(context, request))

       #template = loader.get_template('myfirst.html')
       #return HttpResponse(template.render())
       # return HttpResponse("Hello world!")