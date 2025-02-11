
# Create your views here.

from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
def search(request):
    p= None
    query = ""
    if (request.method == "POST"):
        query = request.POST['q']
        print(query)
        if query:
            p = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context={'product':p,'query':query}
    return render(request,'search.html',context)