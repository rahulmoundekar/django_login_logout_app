import sys
import traceback

from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import auth

from user_login_logout.forms import UserForm
from user_login_logout.models import User, LoginUser


def userLogin(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        try:
            username = request.POST['email']
            password = request.POST['password']
            users = User.objects.filter(email=username, password=password).values()
            if users is not None:
                for user in users:
                    request.session['user_id'] = user['id']
                    request.session['user_email'] = user['email']
                return redirect('/dashboard')
            else:
                messages.error(request, 'Error wrong username/password', extra_tags='alert')
                return redirect('/')
        except Exception as ex:
            # Get current system exception
            ex_type, ex_value, ex_traceback = sys.exc_info()

            # Extract unformatter stack traces as tuples
            trace_back = traceback.extract_tb(ex_traceback)

            # Format stacktrace
            stack_trace = list()

            for trace in trace_back:
                stack_trace.append(
                    "File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))

            print("Exception type : %s " % ex_type.__name__)
            print("Exception message : %s" % ex_value)
            print("Stack trace : %s" % stack_trace)
            messages.error(request, 'Internal Server Error contact to Administrator', extra_tags='alert')
            render(request, 'index.html', {'form': form})

    return render(request, 'index.html', {'form': form})


def userLogout(request):
    form = UserForm(request.POST or None)
    if request.method == 'GET':
        try:
            del request.session['user_id']
        except:
            pass
        messages.success(request, 'You are Logout successfully!', extra_tags='alert')
    return render(request, 'index.html', {'form': form})


def dashboard(request):
    try:
        if request.session['user_id'] is not None:
            print('after login')
            logins = LoginUser.objects.all()
            return render(request, 'user/dashboard.html', {'loginUsers': logins})
        else:
            messages.error(request, 'You are not Authorized User..or Session Expire, Login again', extra_tags='alert')
            return redirect('/')
    except:
        messages.error(request, 'You are not Authorized User..or Session Expire, Login again', extra_tags='alert')
        return redirect('/')


def about(request):
    try:
        if request.session['user_id'] is not None:
            return render(request, 'user/about.html')
        else:
            messages.error(request, 'You are not Authorized User..or Session Expire, Login again', extra_tags='alert')
            return redirect('/')
    except:
        messages.error(request, 'You are not Authorized User..or Session Expire, Login again', extra_tags='alert')
        return redirect('/')


def contact(request):
    try:
        if request.session['user_id'] is not None:
            return render(request, 'user/contact.html')
        else:
            messages.error(request, 'You are not Authorized User..or Session Expire, Login again', extra_tags='alert')
            return redirect('/')
    except:
        messages.error(request, 'You are not Authorized User..or Session Expire, Login again', extra_tags='alert')
        return redirect('/')
