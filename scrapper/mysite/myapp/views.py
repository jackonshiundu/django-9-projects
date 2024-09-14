from django.shortcuts import render
import requests 
from bs4 import BeautifulSoup
from .models import Links
from django.http import HttpResponseRedirect
# Create your views here.

def scrape(request):
    if request.method=='POST':
        site=request.POST.get('site','')
        page=requests.get(site)

        soup=BeautifulSoup(page.text,'html.parser')

        link_address=[]
        for link in soup.find_all('a'):
            link_address=link.get('href')
            link_text=link.string

            Links.objects.create(address=link_address,name=link_text)
        return  HttpResponseRedirect('/')
    else:
        data=Links.objects.all()
    return render(request,'myapp/result.html',{'data':data})

def delete_links(request):
    Links.objects.all().delete()
    return render(request,'myapp/result.html')