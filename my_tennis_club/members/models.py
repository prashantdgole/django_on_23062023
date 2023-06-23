# c:\my_tennis\club\my_tennis_club\members\models.py

from django.db import models
#from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    #author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title}"

class Post(models.Model): # new class to show posts
   text= models.TextField(max_length=255)

   def __str__(self):
      return f"{self.id} {self.text}"
 

class Voucher(models.Model):   # new class
   voucherdate= models.DateField(null=True)
   voucheramount= models.DecimalField(max_digits=16,decimal_places=2, null=True)
   paid_to= models.CharField(max_length=255)
   debitcredit =models.CharField(max_length=15)
   bankorcash= models.CharField(max_length=15)
   narration1= models.CharField(max_length=255)
   narration2= models.CharField(max_length=255)
  
   def __str__(self):
      return f"{self.id} {self.voucherdate}"

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)   # new
  joined_date = models.DateField(null=True) # new
  fees_paid=models.IntegerField(null=True) #new
  fees_balance=models.DecimalField (max_digits = 16,decimal_places = 2 , null=True) #new
  fees_paid_date=models.DateField(null=True) #new

  def __str__(self):
      return f"{self.firstname} {self.lastname}"