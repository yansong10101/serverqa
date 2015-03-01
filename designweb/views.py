from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.forms import UserCreationForm
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from designweb.serializer import *
from designweb.forms import *
from designweb.models import Order, OrderDetails, Category, MicroGroup
from designweb.utils import is_order_list_contain_product, get_display_dict, is_user_already_in_group


def home(request):
    return render(request, 'home.html', get_display_dict(title='HOME'))


def index(request):
    return render(request, 'index.html', {'title': 'HOME', })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            user = authenticate(username=username, password=password)
            # create one to one rel instances for new user
            user.user_profile = UserProfile.objects.create(user=user)
            user.user_profile.first_name = first_name
            user.user_profile.last_name = last_name
            user.user_profile.save()
            user.cart = Cart.objects.create(user=user)
            user.wish_list = WishList.objects.create(user=user)
            login(request, user)
            return render(request, 'home.html', get_display_dict(title='HOME'))
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
            return redirect(reverse('design:home'), get_display_dict(title='HOME'))
        else:
            return render(request, 'login.html', get_display_dict(title='LOGIN'))
    else:
        return render(request, 'login.html', get_display_dict(title='LOGIN'))


def logout_view(request):
    logout(request)
    return redirect(reverse('design:home'))


# first show up for new register customer
@login_required(login_url='/login/')
@api_view(['GET', 'POST', ])
def user_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        if user is not None:
            user.user_profile.gender = request.POST['gender']
            user.user_profile.designer_type = request.POST['designer_type']
            user.user_profile.address1 = request.POST['address1']
            user.user_profile.address2 = request.POST['address2']
            user.user_profile.city = request.POST['city']
            user.user_profile.state = request.POST['state']
            user.user_profile.zip = request.POST['zip']
            user.user_profile.save()
            return redirect(reverse('design:home'), {'title': 'HOME', })
    return render(request, 'user_profile.html', {'title': 'USER PROFILE',
                                                 'designer_type': user.user_profile.designer_type,
                                                 'gender': user.user_profile.gender,
                                                 'address1': user.user_profile.address1,
                                                 'address2': user.user_profile.address2,
                                                 'city': user.user_profile.city,
                                                 'state': user.user_profile.state,
                                                 'zip': user.user_profile.zip,
                                                 'categories': get_display_dict(title='')['categories'],
                                                 })


@ensure_csrf_cookie
def product_view(request, pk):
    user = request.user
    product = get_object_or_404(Product, pk=pk)
    show_create = False
    micro_group = is_user_already_in_group(user, product)
    if micro_group is None:
        show_create = True
    return render(request, 'product.html', {'title': 'PRODUCT',
                                            'pk': product.pk,
                                            'show_create': show_create,
                                            'group': micro_group, })


"""     --Ajax views--      """
@ensure_csrf_cookie
@api_view(['GET', 'POST', ])
def add_cart(request, pk):
    user = request.user
    product = get_object_or_404(Product, pk=pk)
    user.cart.products.add(product)
    return Response(data={'Success': 'Success'})


@ensure_csrf_cookie
@api_view(['GET', 'POST', ])
def add_wish(request, pk):
    user = request.user
    product = get_object_or_404(Product, pk=pk)
    user.wish_list.products.add(product)
    return Response(data={'Success': 'Success'})


@ensure_csrf_cookie
@api_view(['GET', 'POST', ])
def remove_cart(request, pk):
    user = request.user
    product = get_object_or_404(Product, pk=pk)
    user.wish_list.products.remove(product)
    return Response(data={'Success': 'Success'})


@ensure_csrf_cookie
@api_view(['GET', 'POST', ])
def remove_wish(request, pk):
    user = request.user
    product = get_object_or_404(Product, pk=pk)
    user.wish_list.products.remove(product)
    return Response(data={'Success': 'Success'})


@ensure_csrf_cookie
@api_view(['GET', 'POST', ])
@login_required(login_url='/login/')
def update_order_detail(request, pk, num):
    order_detail = get_object_or_404(OrderDetails, pk=pk)
    order_detail.number_items = num
    print('Before -- ' + str(num))
    order_detail.save()
    print('After -- ' + str(order_detail.number_items))
    return Response(data={'Success': 'Success'})


# ===============================================
@ensure_csrf_cookie
@login_required(login_url='/login/')
def my_cart(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user is not None:
        products = user.cart.products.all()
        return render(request, 'mycart.html', {'title': 'MY CART',
                                               'products': products,
                                               'categories': get_display_dict(title='')['categories']})


@ensure_csrf_cookie
@login_required(login_url='/login/')
def my_wish(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user is not None:
        products = user.wish_list.products.all()
        return render(request, 'mywishlist.html', {'title': 'MY WISH LIST',
                                                   'products': products,
                                                   'categories': get_display_dict(title='')['categories']})
# ===============================================


@ensure_csrf_cookie
@login_required(login_url='/login/')
def my_order(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user is not None:
        products = user.cart.products.all()
        order = user.orders.get_or_create(user=user, is_paid=False)[0]
        for item in products:
            if not is_order_list_contain_product(order.details.all(), item.pk):
                OrderDetails.objects.create(order=order, product=item)
        return render(request, 'myorder.html', {'title': 'MY ORDER',
                                                'orders': order.details,
                                                'categories': get_display_dict(title='')['categories']})


def category_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'title': 'CATEGORY',
                                             'products': products,
                                             'categories': get_display_dict(title='')['categories']})


def micro_group_view(request, product_id, group_id=None):
    product = get_object_or_404(Product, pk=product_id)
    show_join = False
    user = request.user

    if product is None:
        return

    if group_id is None or not isinstance(group_id, int):   # inside call
        if user.is_authenticated():
            micro_group = is_user_already_in_group(user, product)
            if micro_group is None:
                # create new group for this user
                group_price = product.price * product.group_discount
                micro_group = MicroGroup.objects.create(product=product, owner=user, is_active=True,
                                                        group_price=group_price, group_discount=product.group_discount)
                micro_group.members.add(user)
            return render(request, 'microgroup.html', {'title': 'M-GROUP',
                                                       'group': micro_group,
                                                       'product': micro_group.product,
                                                       'show_join': show_join, })
        else:
            return redirect(reverse('design:login'), {'title': 'LOGIN', })
    else:   # outside call
        group = get_object_or_404(MicroGroup, pk=group_id)
        if group is not None:
            if not group.objects.filter(user=user).exists():
                show_join = True
            return render(request, 'microgroup.html', {'title': 'M-GROUP',
                                                       'group': group,
                                                       'product': group.product[0],
                                                       'show_join': show_join, })
        else:
            return redirect(reverse('design:home', {'title': 'HOME', }))


# ===============================================
class ProductsList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


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


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
# ===============================================