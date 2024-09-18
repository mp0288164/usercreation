from django.shortcuts import render,redirect
from . forms import *

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
      