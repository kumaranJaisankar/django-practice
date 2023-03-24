from django.shortcuts import render , redirect
from django.contrib.auth.models import User,auth

from django.contrib import messages


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('login')
def indexs(request):
    if request.COOKIES.get('sessionid'):
        ast_visit = request.COOKIES['sessionid']
        if ast_visit is not None:
            return render(request,'index.html')
        else :
            return redirect('login')
    else:
        return redirect('login')
   
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid username or password')
            return redirect('login')
    else :
        return render(request,'userlogin.html')


def registerform(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        new_password = request.POST['password1']
        conform_password= request.POST['password2']
        email= request.POST['email']

        if new_password == conform_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
                return redirect('/accounts/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('/accounts/register')
            else :
                user = User.objects.create_user(username= username,email=email,password=new_password,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('login')
                # return HttpResponse('Successfully created')
           
        else:
            print('password not matching')
        return redirect('/index')
    else:
        return render(request,'reg.html')

