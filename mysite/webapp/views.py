from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordContextMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import *
from django.views.generic import DetailView, UpdateView, DeleteView, FormView, TemplateView
from django.contrib import messages

def info(request):
    return render(request, 'webapp/info_about_dev/info.html')


def members(request):
    list_devs = ('Abylay Sagymbayev', 'Didar Orynbassar')
    return render(request, 'webapp/info_about_dev/members.html', context={'devs': list_devs})


def developers(request):
    addrs = 'Manas Street, 34/1'
    list_devs = ({'name': 'Abylay Sagymbayev', 'phone': '+7 (707) 707-7007', 'email': '27178@iitu.edu.kz', 'hours': '10:00 AM - 04:00 PM'},
                {'name': 'Didar Orynbassar', 'phone': '+7 (707) 707-7008', 'email': '27550@iitu.edu.kz', 'hours': '10:00 AM - 04:00 PM'})
    return render(request, 'webapp/info_about_dev/developers.html', context={'devs': list_devs, 'address': addrs})


def addtocart(request, pk):
    product = Product.objects.get(pk=pk)
    cart = Order_Product.objects.create(owner=request.user, product=product)
    return redirect('home')


def cart(request):
    cart=Order_Product.objects.filter(owner=request.user)
    return render(request, "webapp/cart.html", {'cart': cart})


def index(request):
    # list_furnitures = (
    #     {'src': "/static/webapp/images/brown_armchair.png", 'width': '80%', 'name': 'brown armchair', 'price': '150.00'},
    #     {'src': "/static/webapp/images/bed_design.png", 'width': '100%', 'name': 'Bed Design', 'price': '300.00'},
    #     {'src': "/static/webapp/images/yellow-brown.png", 'width': '70%', 'name': 'House Chair Design', 'price': '200.00'})
    list_furnitures = Product.objects.all()
    return render(request, 'webapp/index.html', context={'furniture': list_furnitures})


def about(request):
    return render(request, 'webapp/about.html')


def furniture(request):
    # list_furnitures = ({'src': "/static/webapp/images/brown_armchair.png", 'width':'80%', 'name':'Brown armchair', 'price':'150.00'},
    #                    {'src': "/static/webapp/images/bed_design.png", 'width':'100%', 'name':'Bed Design', 'price':'300.00'},
    #                    {'src': "/static/webapp/images/yellow-brown.png", 'width':'70%', 'name':'House Chair Design', 'price':'200.00'})
    list_furnitures = Product.objects.all()
    print(list_furnitures)
    return render(request, 'webapp/furniture.html', context={'furniture': list_furnitures})


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully sent!')
    form = ContactUsForm()
    return render(request, 'webapp/contact.html', {"form": form})

def subscribe(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()

    return render(request, 'webapp/index.html')

def adminContactUs(request):
    list_contacts = ContactUs.objects.all()
    return render(request, 'webapp/adminPanel/contactus/adminContactUs.html', context={'contacts': list_contacts})

class ContactDeleteView(DeleteView):
    model = ContactUs
    success_url = '/adminPanel/contacts/'
    template_name = 'webapp/adminPanel/contactus/contactUsDelete.html'

def adminSubscribers(request):
    list_subscribers = Subscriber.objects.all()
    return render(request, 'webapp/adminPanel/subscribers/adminSubscribers.html', context={'subscribers': list_subscribers})

def adminOrders(request):
    list_orders = Order_Product.objects.all()
    return render(request, 'webapp/adminPanel/orders/adminOrders.html',
                  context={'orders': list_orders})

class SubscriberDeleteView(DeleteView):
    model = Subscriber
    success_url = '/adminPanel/subscribers/'
    template_name = 'webapp/adminPanel/subscribers/subscriberDelete.html'

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid value of email or password! Please, try again')
    else:
        form = UserLoginForm()
    return render(request, 'webapp/login.html', {"form": form})

def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered!')
            return redirect('login')
        else:
            messages.error(request, 'Registering error!')
    else:
        form = AccountCreationForm()
    return render(request, 'webapp/registration.html', context={'form': form})

def profile(request):
    return render(request, 'webapp/profile.html')

class ProfileUpdateView(UpdateView):
    model = Account
    template_name = 'webapp/profile.html'
    form_class = AccountForm

    def get_success_url(self):
        return '/'

def adminPanel(request):
    return render(request, 'webapp/adminPanel/adminPanel.html')

def adminAccounts(request):
    list_users = Account.objects.all()
    return render(request, 'webapp/adminPanel/accounts/adminAccounts.html', context={'accounts': list_users})

def accountAdd(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin-accounts')
    else:
        form = AccountCreationForm()
    return render(request, 'webapp/adminPanel/accounts/accountAdd.html', context={'form': form})

class AccountUpdateView(UpdateView):
    model = Account
    template_name = 'webapp/adminPanel/accounts/accountEdit.html'
    form_class = AccountForm

    def get_success_url(self):
        return '/adminPanel/accounts/'

class AccountDeleteView(DeleteView):
    model = Account
    success_url = '/adminPanel/accounts/'
    template_name = 'webapp/adminPanel/accounts/accountDelete.html'

def change_password(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            user = form.save()
            u = Account.objects.get(username__exact=user.email)
            u.set_password('11111')
            u.save()
            #update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
    else:
        form = AccountForm()
    return render(request, 'webapp/adminPanel/accounts/password_change_form.html', {
        'form': form
    })

def adminProducts(request):
    list_furnitures = Product.objects.all()
    return render(request, 'webapp/adminPanel/products/adminProducts.html', context={'furniture': list_furnitures})

def productAdd(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin-products')
    else:
        form = ProductForm()
    return render(request, 'webapp/adminPanel/products/productAdd.html', context={'form': form})

class ProductDetailView(DetailView):
    model = Product
    template_name = 'webapp/adminPanel/products/productDetails.html'
    context_object_name = 'furniture'

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'webapp/adminPanel/products/productEdit.html'
    form_class = ProductForm

    def get_success_url(self):
        return '/adminPanel/products/'

class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/adminPanel/products/'
    template_name = 'webapp/adminPanel/products/productDelete.html'

    # def get_success_url(self):
    #     return '/adminPanel/products/'