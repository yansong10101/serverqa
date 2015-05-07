from django.shortcuts import render, redirect
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
from designweb.utils import *
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
import json
from designweb.caches.group_utils import *


def home(request):
    return render(request, 'home.html', get_display_dict(title='HOME'))


def index(request):
    # print(request.session)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request, 'home.html', {'title': form.cleaned_data['username']})
        else:
            print(form.cleaned_data['error'])
    else:
        form = LoginForm()
    return render(request, 'index.html', {'title': 'HOME', 'form': form, })


def signup(request):
    if request.method == 'POST':
        # username = request.POST['username']
        # password = request.POST['password']
        # confirm_password = request.POST['confirm_password']
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            user.user_profile = UserProfile.objects.create(user=user)
            user.cart = Cart.objects.create(user=user)
            user.wish_list = WishList.objects.create(user=user)
            # sending_mail_for_new_signup(username)
            login(request, user)
            return render(request, 'home.html', get_display_dict(title='HOME', pass_dict={'welcome': True, }))
        else:
            pass_dicts = {'form': form, 'error_msg': form.error_messages}
            return render(request, 'signup.html', get_display_dict('SIGNUP', pass_dict=pass_dicts))
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', get_display_dict('SIGNUP', pass_dict={'form': form, }))


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user.is_authenticated():
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
            return redirect(reverse('design:home'), get_display_dict('HOME'))

    pass_dicts = {'designer_type': user.user_profile.designer_type,
                  'gender': user.user_profile.gender,
                  'address1': user.user_profile.address1,
                  'address2': user.user_profile.address2,
                  'city': user.user_profile.city,
                  'state': user.user_profile.state,
                  'zip': user.user_profile.zip, }
    return render(request, 'user_profile.html', get_display_dict('USER PROFILE', pass_dict=pass_dicts))


@ensure_csrf_cookie
def product_view(request, pk):
    user = request.user
    product = get_object_or_404(Product, pk=pk)
    show_create = False
    micro_group = is_user_already_in_group(user, product)
    if micro_group is None:
        show_create = True
    image_dict = get_s3_bucket_image_by_product(product.product_code)
    pass_dicts = {'product': product,
                  'show_create': show_create,
                  'group': micro_group,
                  'is_in_cart': is_product_in_user_cart(user, pk)}
    return render(request,
                  'product.html',
                  (get_display_dict('PRODUCT', pass_dict=dict(list(image_dict.items()) + list(pass_dicts.items())))))


"""     --Ajax views--      """
@ensure_csrf_cookie
@api_view(['GET', 'POST', ])
def add_cart(request, pk, prod_quantity=1):
    user = request.user
    product = get_object_or_404(Product, pk=pk)
    user.cart.products.add(product)
    if not is_product_in_cart_details(user, product):
        user.cart.cart_details.create(cart=user.cart, product=product, number_in_cart=prod_quantity)
    else:
        cart_detail = user.cart.cart_details.filter(product=product)[0]
        cart_detail.number_in_cart = prod_quantity
        cart_detail.save()
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
    user.cart.products.remove(product)
    if is_product_in_cart_details(user, product):
        user.cart.cart_details.filter(product=product).delete()
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
    order_detail.save()
    return Response(data={'Success': 'Success'})


@ensure_csrf_cookie
@api_view(['GET', 'POST', ])
@login_required(login_url='/login/')
def update_cart_detail(request, pk, num, order_id=None):
    cart_detail = get_object_or_404(CartDetail, pk=pk)
    cart_detail.number_in_cart = num
    cart_detail.save()
    cost_dict = calc_all_price_per_order(order_id)
    cost_dict['Success'] = 'Success'
    return Response(data=cost_dict)


@ensure_csrf_cookie
@api_view(['GET', 'POST', ])
def like_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.number_like += 1
    product.save()
    return Response(data={'Success': 'Success'})


@ensure_csrf_cookie
@api_view(['GET', 'POST', ])
def get_product_review(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = CustomerReview.objects.filter(product=product)
    # return Response(data={'review_list': reviews})
    return Response(data={'Success': 'Success'})


def get_product_forum(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = ProductComment.objects.filter(product=product)
    return Response(data={'Success': 'Success', 'comments': comments})

# ===============================================
@ensure_csrf_cookie
@login_required(login_url='/login/')
def my_cart(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user.is_authenticated():
        products = user.cart.products.all()
        order_dicts = order_view_process(user)
        pass_dicts = {'products': products, 'orders': user.cart.cart_details.all()}
        combine_dicts = dict(list(order_dicts.items()) + list(pass_dicts.items()))
        return render(request, 'mycart.html', get_display_dict('MY CART', pass_dict=combine_dicts))


@ensure_csrf_cookie
@login_required(login_url='/login/')
def my_wish(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user is not None:
        products = user.wish_list.products.all()
        pass_dicts = {'products': products, }
        return render(request, 'mywishlist.html', get_display_dict('MY WISH LIST', pass_dict=pass_dicts))
# ===============================================


def category_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category)
    pass_dicts = {'products': products, }
    return render(request, 'category.html', get_display_dict('CATEGORY', pass_dict=pass_dicts))


def micro_group_view(request, product_id, group_id=None):
    product = get_object_or_404(Product, pk=product_id)
    show_join = False
    user = request.user

    if product is None:
        return

    if group_id is None or not isinstance(group_id, int):   # inside call -- create or to product page
        if user.is_authenticated():
            micro_group = is_user_already_in_group(user, product)
            if micro_group is None:
                # create new group for this user
                group_price = product.price * product.group_discount
                micro_group = MicroGroup.objects.create(product=product, owner=user, is_active=True,
                                                        group_price=group_price, group_discount=product.group_discount)
                micro_group.members.add(user)
                # update cache <timestamp_group_cache> & <user_group_cache>
                update_caches_by_new_group(user, micro_group)
            total_members = micro_group.members.count()
            pass_dicts = {'group': micro_group,
                          'product': micro_group.product,
                          'show_join': show_join,
                          'remain_time': micro_group.get_remain_time_by_seconds(),
                          'total_members': total_members, }
            return render(request, 'microgroup.html', get_display_dict('M-GROUP', pass_dict=pass_dicts))
        else:
            return redirect(reverse('design:login'), get_display_dict('LOGIN'))
    else:   # outside call -- group page or to product page
        group = get_object_or_404(MicroGroup, pk=group_id)
        if group is not None:
            total_members = group.members.count()
            if not group.objects.filter(user=user).exists():
                show_join = True
            pass_dicts = {'group': group,
                          'product': group.product[0],
                          'show_join': show_join,
                          'remain_time': group.get_remain_time_by_seconds(),
                          'total_members': total_members, }
            return render(request, 'microgroup.html', get_display_dict('M-GROUP', pass_dict=pass_dicts))
        else:
            return redirect(reverse('design:product-view', kwargs={'pk': product_id}), get_display_dict('PRODUCT'))


@ensure_csrf_cookie
@login_required(login_url='/login/')
def update_order_info(request, pk, order_id):
    shipping_data = {
        'shipping_address1': request.POST.get('shipping_address1'),
        'shipping_address2': request.POST.get('shipping_address2'),
        'shipping_city': request.POST.get('shipping_city'),
        'shipping_state': request.POST.get('shipping_state'),
        'shipping_zip': request.POST.get('shipping_zip'),
        'shipping_phone1': request.POST.get('shipping_phone1'),
        'shipping_phone2': request.POST.get('shipping_phone2'),
        'billing_address1': request.POST.get('billing_address1'),
        'billing_address2': request.POST.get('billing_address2'),
        'billing_city': request.POST.get('billing_city'),
        'billing_state': request.POST.get('billing_state'),
        'billing_zip': request.POST.get('billing_zip'),
        'billing_phone1': request.POST.get('billing_phone1'),
        'billing_phone2': request.POST.get('billing_phone2'),
    }

    msg = update_order_address_info(pk, order_id, shipping_data)
    response_data = {}
    try:
        response_data['result'] = 'writing successful !'
    except:
        response_data['message'] = 'failed processing ...\n' + msg
    return HttpResponse(json.dumps(response_data), content_type='application/json')


# ================ api =======================
class ProductsList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer


class ProductReviewList(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReviewSerializer


class CustomerList(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReviewSet(viewsets.ModelViewSet):
    queryset = CustomerReview.objects.all()
    serializer_class = ProductReviewSerializer
    filter_fields = ('product_id', )


class ProductForumList(viewsets.ReadOnlyModelViewSet):
    queryset = ProductComment.objects.all()
    serializer_class = ProductForumListSerializer
    filter_fields = ('product_id', )
    paginate_by = 5


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
# ===============================================


# ==================== payment pages =============
# for paypal redirect usage
def payment_view(request):
    from designweb.payment.payment_utils import payment_execute
    payment_dict = payment_execute(request.GET['paymentId'], request.GET['PayerID'], request.GET['token'])
    print(payment_dict)
    return redirect(reverse('design:payment-success'),
                    get_display_dict(title='Payment Success', pass_dict=payment_dict))


def payment_success(request):
    return render(request, 'payment/payment_success.html', get_display_dict(title='Payment Success'))


def payment_failed(request):
    return render(request, 'payment/payment_fail.html', get_display_dict(title='Payment Failed'))


def checkout(request):
    print(request.POST['holder_name'])
    print(request.POST['expired_month'])

    from designweb.payment.payment_utils import payment_process
    payment_dict = payment_process('paypal', request.META['HTTP_HOST'])
    if not payment_dict:
        return render(request, 'payment/payment_fail.html', get_display_dict(title='Payment Failed'))
    redirect_url = payment_dict['redirect_url']
    if redirect_url:    # payment method is paypal
        return HttpResponseRedirect(redirect_url)
    else:
        print(payment_dict)
        return redirect(reverse('design:payment-success'),
                        get_display_dict(title='Payment Success', pass_dict=payment_dict))
# ===============================================
