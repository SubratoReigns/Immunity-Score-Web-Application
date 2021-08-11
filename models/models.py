from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True,blank=True)
    anaemia = models.IntegerField(null=True,blank=True)
    crePhos = models.IntegerField(null=True,blank=True)
    diab = models.IntegerField(null=True,blank=True)
    ejecFrac = models.IntegerField(null=True,blank=True)
    highbp = models.IntegerField(null=True,blank=True)
    platecount = models.IntegerField(null=True,blank=True)
    serumcre = models.FloatField(null=True,max_length = 5)
    serumsod = models.IntegerField(null=True,blank=True)
    sex = models.IntegerField(null=True,blank=True)
    smoke = models.IntegerField(null=True,blank=True)
    time = models.IntegerField(null=True,blank=True)
    Heart_Result = models.CharField(null=True,max_length=13)
    Immunity_Status= models.CharField(null=True, blank=True,max_length=13)
    timestamp = models.DateTimeField(null=True,default=now)

class DiabetesPatient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    preg = models.IntegerField(null=True,blank=True)
    gluc = models.IntegerField(null=True,blank=True)
    bp = models.IntegerField(null=True,blank=True)
    skinthick = models.IntegerField(null=True,blank=True)
    insul = models.IntegerField(null=True,blank=True)
    bmi = models.FloatField(null=True,max_length=5)
    diabpedfun = models.FloatField(null=True,max_length=5)
    age = models.IntegerField(null=True,blank=True)
    Diabetes_Result = models.CharField(null=True,max_length=13)
    Immunity_Status= models.CharField(null=True, blank=True,max_length=13)
    timestamp = models.DateTimeField(null=True,default=now)
    




    

