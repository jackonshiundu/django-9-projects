from django.shortcuts import render
from .models import Products,Orders
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    products=Products.objects.all()

    #search functionality
    search_item=request.GET.get('search_item')
    if search_item !='' and search_item is not None:
        products= Products.objects.filter(name__icontains=search_item)
    
    #paginator
    paginator=Paginator(products,4)
    page=request.GET.get('page')
    products=paginator.get_page(page)

    return render(request,'shop/index.html',{'products':products})


def detail(request,id):
    product_item=Products.objects.get(id=id)

    return render(request,'shop/detail_page.html',{'product_item':product_item})


def checkout(request):

    if request.method == "POST":
        items=request.POST.get("items","")
        name=request.POST.get("name","")
        email=request.POST.get("email","")
        address=request.POST.get("address","")
        city=request.POST.get("city","")
        state=request.POST.get("state","")
        zip=request.POST.get("zip","")
        total=request.POST.get('total',"")
        order=Orders(items=items,name=name,email=email,address=address,city=city,state=state,zip=zip,total=total)
        order.save()
    return render(request,'shop/checkout.html')