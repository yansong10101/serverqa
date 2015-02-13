from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.forms import UserCreationForm
from rest_framework import generics, viewsets
from designweb.serializer import *
from designweb.forms import *


def home(request):
    return render(request, 'home.html', {'title': 'HOME', })


def index(request):
    return render(request, 'index.html', {'title': 'HOME', })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'user_profile.html', {'title': 'USER PROFILE'})
        else:
            return render(request, 'signup.html', {'form': form, 'title': 'SIGNUP', 'error_msg': form.error_messages})
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
            # return redirect(reverse('home.html'))
            return render(request, 'home.html', {'title': 'HOME', })
        else:
            return render(request, 'login.html', {'title': 'LOGIN', })
    else:
        return render(request, 'login.html', {'title': 'LOGIN', })


def logout_view(request):
    logout(request)
    return redirect(reverse('design:home'))


# first show up for new signup customer, for adding profile details
@login_required(login_url='/login/')
def user_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user_profile_form = UserProfileForm(request.POST, prefix='user-profile')
        if user_profile_form.is_valid():
            # user_profile_form.
            user_profile_form.save(commit=False)
            return render(request, 'user_profile.html', {'title': 'USER PROFILE', 'form': user_profile_form})
    else:
        user_profile_form = UserProfileForm()
    return render(request, 'user_profile.html', {'title': 'USER PROFILE', 'form': user_profile_form})


@ensure_csrf_cookie
def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', {'title': 'PRODUCT', 'pk': product.pk})


def my_cart(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'mycart.html', {'title': 'MY CART', 'pk': user.pk})


class ProductsList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    #
    # def get_queryset(self):
    #     queryset = Product.objects.all()
    #     image_root = self.request.


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
