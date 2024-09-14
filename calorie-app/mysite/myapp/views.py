from django.shortcuts import render,redirect
from .models import Food,Consume
# Create your views here.

def index(request):
    if request.method == "POST":
        food_consume=request.POST['food_consume']
        consume=Food.objects.get(name=food_consume)
        user =request.user

        consume_obj=Consume(user=user,food_consumed=consume)
        consume_obj.save()
        foods=Food.objects.all()
        consumed_food=Consume.objects.filter(user=request.user)

    else:
        consumed_food=Consume.objects.filter(user=request.user)
        foods=Food.objects.all()

    return render(request,'myapp/index.html',{'foods':foods,'consumed_food':consumed_food})

def delete_consume(request,id):
    consume_food=Consume.objects.get(id=id)
    if request.method=="POST":
        consume_food.delete()

        return redirect('/') 
    
    return render(request,'myapp/delete.html')