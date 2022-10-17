from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Product
from .forms import OrdersForm

# Create your views here.


def homes(request):
    price = {
        "onion_price": Product.objects.get(PRDName='Onions'),
        "carrot_price": Product.objects.get(PRDName='Carrots'),
        "potatoe_price": Product.objects.get(PRDName='Potatoes'),
    }
    return render(request, 'index.html', price)


def orders(request):
    form = OrdersForm(request.POST or None)
    if form.is_valid():
        form.save()
    messages.success(request, ("This is good"))
    return render(request, 'user_input.html', {'form': form})


"""
def stock(requst):
    product_list = Product.objects.all()
    context = {'product_list': product_list}

    return render(requst, 'home.html', context)


def order(request):  # id
    #product_details = Product.objects.get(id=id)
    #context = {'product_details': product_details}

    return render(request, 'order.html', )


def potatoes(request):  # id
    #product_details = Product.objects.get(id=id)
    #context = {'product_details': product_details}

    return render(request, 'parts/navbar.html',)


def cart(request):
    return render(request, 'cart.html')



    price = {
        "onion_price": Product.objects.get(PRDName='onions'),
        "carrot_price": Product.objects.get(PRDName='carrots'),
        "potatoe_price": Product.objects.get(PRDName='potatoes'),
    }

    x = requst.POST.get('onions_quantity')
    y = requst.POST.get('carrots_quantity')
    z = requst.POST.get('potatoes_quantity')
    data = Order(onions_quantity=x, carrots_quantity=y, potatoes_quantity=z)
    # data.save()
"""
