from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import *
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import ensure_csrf_cookie
from designweb import tests


def test_page(request):
    return render(request, 'index.html')


# Create your views here.
def index(request):
    user = request.user
    if not user.is_anonymous():
        return HttpResponse("Hello, " + user.username)
    else:
        # user = tests.db_read()
        return HttpResponse('this is anonymous user...')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse(index))     # need redirect to successful page, or to home page and show msg
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('design:index'))
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect(reverse('design:index'))