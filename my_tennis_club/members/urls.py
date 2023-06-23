# my_tennis_club\my_tennis_club/members/urls.py:

from django.urls import  path
from . import views

urlpatterns = [
  path('', views.main, name='main'),
  path('vouchersmain/',views.vouchersmain,name='vouchersmain'),
  path('vouchers/',views.vouchers,name='vouchers'),
  path('vadd/',views.vadd,name='vadd'),
  path('vadd/voucheraddrecord/',views.voucheraddrecord,name='voucheraddrecord'),
  path('vedit/',views.vedit,name='vedit'),
  path('vedit/vouchereditdetails/<int:id>',views.vouchereditdetails,name='vouchereditdetails'),
  path('vdelete/',views.vdelete,name='vdelete'),
  path('vdelete/voucherdeletedetails/<int:id>',views.voucherdeletedetails,name='voucherdeletedetails'),
  path('vdelete/voucherdeletedetails/voucherdeleterecord/<int:id>',views.voucherdeleterecord,name='voucherdeleterecord'),
  path('vedit/vouchereditdetails/vouchereditrecord/<int:id>',views.vouchereditrecord,name='vouchereditrecord'),
  path('mdelete/', views.mdelete, name='mdelete'),
  path('testing/', views.testing, name='testing'),
  path('posts/',views.posts,name='all_posts'),
  path('blogs/',views.blogs,name='all_blogs'),
  path('members/', views.members, name='members'),
  path('mshow/details/<int:id>', views.details, name='details'),
  path('madd/', views.madd, name='madd'),
  path('madd/addrecord/', views.addrecord, name='addrecord'),
  path('mshow/', views.mshow, name='mshow'),
  path('medit/', views.medit, name='medit'),
  path('medit/membeditdetails/<int:id>',views.membeditdetails,name='membeditdetails'),
  path('medit/membeditdetails/editrecord/<int:id>',views.editrecord,name='editrecord'),
  path('mdelete/', views.mdelete, name='mdelete'),
  path('mdelete/membdeletedetails/<int:id>',views.membdeletedetails,name='membdeletedetails'),
  path('mdelete/membdeletedetails/deleterecord/<int:id>',views.deleterecord,name='deleterecord'),
]