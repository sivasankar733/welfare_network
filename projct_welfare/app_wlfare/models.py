from django.db import models

from django.db import models


class RegistrationModel(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    pas=models.CharField(max_length=15)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    con=models.IntegerField(unique=True)
    dob=models.DateField()
    companynam=models.CharField(max_length=40)
    status = models.CharField(max_length=30,default=False)


class UserthoughtsModel(models.Model):
    name=models.CharField(max_length=40)
    description=models.CharField(max_length=100)
    contact=models.IntegerField(unique=True)

class EventsModel(models.Model):
    name=models.CharField(max_length=40)
    startdate=models.DateField()
    enddate=models.DateField()
    description=models.CharField(max_length=100)
    contactno=models.IntegerField(unique=True)

class TechnicalModel(models.Model):
    name=models.CharField(max_length=40)
    technology=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    contactno=models.IntegerField(unique=True)

class WorkexperienceModel(models.Model):
    name=models.CharField(max_length=40)
    technology=models.CharField(max_length=40)
    workexperience=models.IntegerField()
    description=models.CharField(max_length=50)
    contactno=models.IntegerField(unique=True)

class PropertyModel(models.Model):
    name=models.CharField(max_length=40)
    property_type=models.CharField(max_length=50)
    property_title=models.CharField(max_length=100)
    area_size=models.IntegerField()
    price=models.FloatField()
    address=models.CharField(max_length=100)
    contactno=models.IntegerField(unique=True)
    email=models.EmailField(unique=True)

class SharemarketModel(models.Model):
    name=models.CharField(max_length=40)
    copmany_name=models.CharField(max_length=50)
    share_value=models.IntegerField()
    description=models.CharField(max_length=100)

class ReferencesModel(models.Model):
    name=models.CharField(max_length=40)
    job_title=models.CharField(max_length=100)
    description=models.CharField(max_length=70)
    lastdate=models.DateField()

class matrimonialModel(models.Model):
    brifegrom_name=models.CharField(max_length=40)
    gender=models.CharField(max_length=10)
    dob=models.DateField()
    description=models.CharField(max_length=100)
    contactno=models.IntegerField(unique=True)

class CelebrationsModel(models.Model):
    name=models.CharField(max_length=40)
    address=models.CharField(max_length=200)
    contactno=models.IntegerField(unique=True)
    email=models.EmailField(unique=True)
    dob=models.DateField()

class TravelModel(models.Model):
    name=models.CharField(max_length=40)
    travel_date=models.DateField()
    location=models.CharField(max_length=200)
    description=models.CharField(max_length=100)
    contactno=models.IntegerField(unique=True)

class AdminModel(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=40)
    pas=models.CharField(max_length=20)
    address=models.CharField(max_length=500)
    email=models.EmailField(unique=True)
    contactno=models.IntegerField(unique=True)
    dob=models.DateField()
    companyname=models.CharField(max_length=100)
    status=models.CharField(max_length=20)
