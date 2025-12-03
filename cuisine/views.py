from django.shortcuts import render, get_object_or_404
from .models import Cuisine
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView

# Create your views here.

class CuisineListView(ListView):
    queryset = Cuisine.objects.all()
    context_object_name='cuisines'
    paginate_by=3
    template_name='cuisine/cuisine/list.html'

class CuisineDetailView(DetailView):
    model = Cuisine
    context_object_name = 'cuisine'
    template_name = 'cuisine/cuisine/detail.html'


def Cuisine_list(request):
    object_list = Cuisine.objects.all()
    paginator = Paginator(object_list,3)
    page = request.GET.get('page')
    try:
        cuisines=paginator.page(page)
    except PageNotAnInteger:
        cuisines =paginator.page(1)
    except EmptyPage:
        cuisines = paginator.page(paginator.num_pages)

    return render(
        request,
        'cuisine/cuisine/list.html',
        {'page':page,'cuisines': cuisines}
    )

def cuisine_detail(request, cuisine):
    cuisineClicked = get_object_or_404(
        Cuisine,
        slug=cuisine,
        status='published'
    )
    return render(
        request,
        'cuisine/cuisine/detail.html',
        {'cuisine': cuisineClicked}
    )
