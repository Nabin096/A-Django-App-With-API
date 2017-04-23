from django.db import models
from django.core.urlresolvers import reverse

class profiles(models.Model):
    username=models.CharField(max_length=250,default='ok')
    password= models.CharField(max_length=50,default='k')
    code1= models.CharField(max_length=250,null=True)
    code2= models.CharField(max_length=250,null=True)
    code3= models.CharField(max_length=250,null=True)
    code4= models.CharField(max_length=250,null=True)
    code5= models.CharField(max_length=250,null=True)
    code6= models.CharField(max_length=250,null=True)
    status= models.IntegerField(default=1)
    filled =models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('login:dashboard', kwargs= {'pk':self.pk})

    def __str__(self):
       return self.username + ' - ' + self.password

