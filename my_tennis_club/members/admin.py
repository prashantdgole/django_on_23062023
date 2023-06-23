# c:\my_tennis_club\my_tennis_club\members\admin.py

from django.contrib import admin
from .models import Member  # new to include members in admin screen
from .models import Voucher # new to include voucher in admin screen

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)

class VoucherAdmin(admin.ModelAdmin):
  list_display = ("paid_to", "voucherdate", "voucheramount","narration1","narration2",)


admin.site.register(Member, MemberAdmin)   # new
admin.site.register(Voucher, VoucherAdmin) # new
#admin.site.register(Member)   # new