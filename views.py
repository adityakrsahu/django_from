from django.shortcuts import render
from .models import *
# Create your views here.

#View for Register Page

def RegisterPage(request):
    return render(request,"app/register.html")



# View for user registration
def UserRegister(request):

    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        # First we will validate that user already exist
        user = User.objects.filter(Email=email)

        if user: 
            message = "User already exist"
            return render(request,"app/register.html",{'msg':message})
        else:
            if password == cpassword:
                newuser = User.objects.create(Firstname=fname,Lastname=lname,Email=email
                                    ,Contact=contact,Password=password)
                message = "User register Successfully"
                return render(request,"app/login.html",{'msg':message})
            else:
                message = "Password and Confirm Password Does not Match"
                return render(request,"app/register.html",{'msg':message})



#Login VIew

def LoginPage(request):
    return render(request,"app/login.html")


# Login User
def LoginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Checking the emailid with database
        user = User.objects.filter(Email=email)
        if user:
            data = User.objects.get(Email=email)
            if data.Password == password:
                
                # change bad me 
                fname=data.Firstname
                lname=data.Lastname
                email=data.Email
                contact=data.Contact
                
                user={
                    'fname':fname,
                    'lname':lname,
                    'email':email,
                    'contact':contact,
                }
                # We are getting user data in session
                # coment bad me
                # request.session['Firstname'] = data.Firstname
                # request.session['Lastname'] = data.Lastname
                # request.session['Email'] = data.Email
                
                return render(request,"app/home.html",user)
            else:
                message = "Password does not match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message = "User does not exist"
            return render(request,"app/register.html",{'msg':message})