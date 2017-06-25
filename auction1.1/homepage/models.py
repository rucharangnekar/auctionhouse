from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils import timezone

# Create your models here.


class Item(models.Model):
    item_price = models.IntegerField(max_length=100)
    item_title = models.CharField(max_length=250)
    item_pic = models.CharField(max_length=1000)
    item_id=models.IntegerField(max_length=10)
    item_desc = models.CharField(max_length=1000, default='')
    item_bidprice = models.IntegerField(max_length=100)
    item_enddate = models.DateField(default=timezone.now())
    item_owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def get_absolute_url(self):
        return reverse('homepage:detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.item_title + ' - ' +self.item_title



class Painting(models.Model):
    painting_price = models.IntegerField(max_length=100)
    painting_title = models.CharField(max_length=250)
    painting_pic = models.CharField(max_length=1000)
    painting_id = models.IntegerField(max_length=10)
    painting_desc = models.CharField(max_length=1000, default='')
    painting_bidprice = models.IntegerField(max_length=100)
    painting_enddate = models.DateField(default=timezone.now())
    painting_owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def get_absolute_url(self):
        return reverse('homepage:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.painting_title + ' - ' + self.painting_title


class Antique(models.Model):
    antique_price = models.IntegerField(max_length=100)
    antique_title = models.CharField(max_length=250)
    antique_pic = models.CharField(max_length=1000)
    antique_id = models.IntegerField(max_length=10)
    antique_desc = models.CharField(max_length=1000, default='')
    antique_bidprice = models.IntegerField(max_length=100)
    antique_enddate = models.DateField(default=timezone.now())
    antique_owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def get_absolute_url(self):
        return reverse('homepage:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.antique_title + ' - ' + self.antique_title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    auc_id1 = models.ForeignKey(Item, on_delete=models.CASCADE, default=1)
    auc_id2 = models.ForeignKey(Painting, on_delete=models.CASCADE, default=1)
    auc_id3 = models.ForeignKey(Antique, on_delete=models.CASCADE, default=1)
    price = models.IntegerField(max_length=100, null=True)
    pic = models.CharField(max_length=1000)


class Myuser(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    country = models.CharField(max_length=250,null=True)
    price = models.IntegerField(max_length=100,default=0,null=True)
    contact = models.IntegerField(max_length=10,default=0,null=True)
    fname = models.CharField(max_length=10,null=True)
    lname = models.CharField(max_length=10,null=True)
    address = models.CharField(max_length=10,null=True)
    email = models.CharField(max_length=100,null=True)
    code = models.IntegerField(max_length=1000,default=0,null=True)


class Bill(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    billid = models.AutoField(primary_key=True)
