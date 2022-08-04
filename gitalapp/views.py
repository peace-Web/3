from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Order, Package
from django.contrib import messages
# Create your views here.


def index(request):
    packages = Package.objects.all()
    context = {
        "packages": packages
    }
    return render(request, "gitalapp/index.html", context)


def order(request, pk):
    package = Package.objects.get(id=pk)
    context = {
        "package": package
    }
    return render(request, 'gitalapp/order.html', context)


def makeorder(request):
    # packaged = Package.objects.get(id=pk)
    fname = request.POST["fname"]
    lname = request.POST["lname"]
    phone = request.POST["phone"]
    email = request.POST["email"]
    package = request.POST["package"]
    pay = request.POST["pay"]
    order = Order(first_name=fname, last_name=lname,
                  email=email, phone=phone, package=package, pay_gateway=pay)
    order.save()
    messages.info(
        request, "Thanks, Your order was placed successfully we will contact you soon.")

    return HttpResponseRedirect(reverse('gitalapp/index'))
