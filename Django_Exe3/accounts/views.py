from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            User.obcjects.create_user(username=form.instance.username,
                                      password=form.instance.password,
                                      email=form.instance.email,
                                      last_name=form.instance.last_name)

            user=User.objects.get(username=form.instance.username)

            return redirect('/')
        else:
            return redirect('sign_up')
    else:
        form=SignUpForm
    return render(request,'accounts/sign_up.html',{
        'form':form,
    })

