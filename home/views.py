from django.shortcuts import render, HttpResponse,  get_object_or_404
from home.models import Product

# Create your views here.
def index(request):
    context ={
        'variable':"this is sent"
    }
    return render(request, 'index.html',context)
    # return HttpResponse("this is homepage")
def home(request):
    return HttpResponse("This is home layout.")


def about(request):
    return HttpResponse("Hello world!")

def services(request):
    return HttpResponse("Hello world!sfdhjk")

def home(request):
    products = Product.objects.all()
    return render(request, 'home/index.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'home/product_detail.html', {'product': product})




# Harry tell about some websites
###Bootstrap