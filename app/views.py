from django.shortcuts import render
from .models import *
from random import randint
from .utils import *
# Create your views here.

def RegistrationPage(request):
    return render(request,"app/register.html")

def LoginPage(request):
    return render(request,"app/login.html")
    
def ImagePage(request):
    return render(request,"app/image.html")

def JsPage(request):
    return render(request,"app/jsDemo.html")

def RegisterUser(request):
    try:
        if request.POST['role']=="doctor":
            role = request.POST['role']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            password = request.POST['password']
            confirmpassword = request.POST['confirmpassword']
            gender = request.POST['gender']
            email = request.POST['email']
            speciality = request.POST['speciality']
            dateofbirth = request.POST['birthdate']
            city = request.POST['city']
            mobile = str(request.POST['phone'])

            user = User.objects.filter(email=email)
            if user:
                # This is our first validation on server side
                message = "User already Exist"
                return render(request,"app/register.html",{'message':message})
            else:
                if password==confirmpassword:
                    otp = randint(10000,99999)
                    newuser = User.objects.create(role=role,email=email,password=password,otp=otp)
                    newdoctor = Doctor.objects.create(user_id=newuser,firstname=firstname,lastname=lastname,gender=gender,speciality=speciality,birthdate=dateofbirth,
                                                        city=city,mobile=mobile)
                    email_subject = "Account Verification"
                    sendmail(email_subject,"mail_template",email,{'name':firstname,'otp':otp})
                    return render(request,"app/login.html")
                else:
                    message = "Password doesnot match"
                    return render(request,"app/register.html",{'message':message})

    except Exception as e1:
        print("Registration Exception -------------->",e1)



def LoginUser(request):
    if request.POST['role']=="doctor":
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.get(email=email) # Master Table Data
        if user:
            if user.password==password and user.role=="doctor":
                doctor = Doctor.objects.get(user_id=user)   # Child Table Data
                request.session['firstname'] = doctor.firstname
                request.session['id'] = user.id
                request.session['email'] = user.email
                request.session['lastname'] = doctor.lastname

                return render(request,"app/home.html")

            else:
                message = "Password and role doesnot match"
                return render(request,"app/login.html",{'message':message})
        else:
            message = "User doesnot exist"
            return render(request,"app/login.html",{'message':message})
    else:
        print("Paitent Area")



def ImageUpload(request):
    image = request.FILES['image']
    newimg = FileUpload.objects.create(image=image)
    message ="File Uploaded"
    return render(request,"app/image.html",{'message':message})


def FetchFile(request):
    all_img = FileUpload.objects.all()
    return render(request,"app/image.html",{'all_img':all_img})