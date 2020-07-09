from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now=True)
    is_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class Doctor(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100, blank= True)
    speciality = models.CharField(max_length = 100)
    mobile = models.CharField(max_length = 10)
    clinic = models.CharField(max_length= 100,blank = True)
    address = models.CharField(max_length= 500, blank= True)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50, blank= True)
    gender = models.CharField(max_length= 10)
    birthdate = models.DateField()
    location = models.CharField(max_length= 30, blank= True)
    about_doc = models.CharField(max_length= 100, blank= True)
    profile_pic=models.FileField(upload_to='app/img/',default='doc_male.png')

class Patient(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    mobile = models.CharField(max_length = 10)
    address = models.CharField(max_length= 500, blank = True)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50, blank = True)
    gender = models.CharField(max_length= 10)
    birthdate = models.DateField()

    #updated patient profile

    blood_group=models.CharField(max_length=10,blank= True)
    blood_presure=models.CharField(max_length=10,blank= True)
    sugar=models.CharField(max_length=10,blank= True)
    Haemoglobin=models.CharField(max_length=10,blank= True)
    profile_pic=models.FileField(upload_to='app/img/',default='patient_icon.png')


class FileUpload(models.Model):
    image = models.ImageField(upload_to="img/")