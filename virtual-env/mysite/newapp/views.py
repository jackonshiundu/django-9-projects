from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator
# Create your views here.


def Movie_list(request):
    movies_objects=Movies.objects.all()

    movie_name=request.GET.get('movie_name')
    if movie_name!='' and movie_name is not None:
        movies_objects=Movies.objects.filter(name__icontains=movie_name)
    #pagination code
    paginator=Paginator(movies_objects,5)
    page=request.GET.get('page')
    movies_objects=paginator.get_page(page)
    return render(request,'newapp/movie_list.html',{'movies_objects':movies_objects})