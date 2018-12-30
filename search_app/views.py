from django.shortcuts import render
from search_app.forms import SearchForm
from . import list_generator

# Create your views here.
def index(request):
    form = SearchForm()
    if request.method=="POST":
            form = SearchForm(request.POST)
            if form.is_valid():
                search_album = form.cleaned_data['search_album']
                search_artist = form.cleaned_data['search_artist']
                print("Topic is",search_artist)

                result = list_generator.LIST(search_album,search_artist).throwlist()
                return render(request,"list.html",{'form':form,'result':result})

    return render(request,"index.html",{'form':form})


# def
