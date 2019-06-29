
from django.db import models
import datetime
from datetime import date 


class ToDo(models.Model):
   text = models.CharField(max_length=250, unique=True)
   done = models.BooleanField()
   cuDate =  models.DateField(("Date"), default=datetime.date.today)
   expDate = models.CharField(max_length=250, unique=True)
   
# class ToDoDone(models.Model):
#    idDone = models.ForeignKey(ToDo, on_delete=models.CASCADE)
#    text = models.CharField(max_length=250, unique=True)
#    done = models.BooleanField()
#    cuDate =  models.DateField(("Date"), default=datetime.date.today)
#    expDate = models.CharField(max_length=250, unique=True)
    




