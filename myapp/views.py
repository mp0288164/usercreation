from django.shortcuts import render,redirect
from . forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


#____inedx or home____________
def indexview(request):
    return render(request,'index.html')


#________login_______________
def loginview(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('afterlogin')
        else:
            return HttpResponse("username or password is incorrect")

    return render(request,'login.html')

#_____afterlogin____
def afterloginview(request):
    return render(request,'afterlogin.html')

#_____logout_____
def logoutview(request):
    logout(request)
    return redirect("index")

#_____userregistration____
def userview(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to the database
            return redirect('success')  # Redirect to a success page
    else:
        form = UserForm()
    return render(request, 'user_reg.html', {'form': form})

def successview(request):
    return render(request, 'success.html')
      