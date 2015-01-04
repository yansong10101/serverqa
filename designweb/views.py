from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import *
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import ensure_csrf_cookie

from designweb import tests


# Create your views here.
@ensure_csrf_cookie
def index(request):
    if request.user is not None:
        user = request.user
        return HttpResponse("Hello, " + user.username)
    else:
        user = tests.db_read()
        return HttpResponse(user)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request['username']
            password = request['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse(index))     # need redirect to successful page, or to home page and show msg
        else:
            render(request, 'signup.html', {'form': form})
    else:   # To Do - do we need specify 'GET' method here?
        pass


def login(request):
    if request.method == 'POST':
        username = request['username']
        password = request['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse(index))     # need redirect to membership home page
        else:
            render(request, 'login.html')
    else:   # To Do - do we need specify 'GET' method here?
        pass


def logout(request):
    logout(request)
    return redirect(reverse(index))