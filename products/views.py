from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
# Create your views here.

def index(request):
    alphabetical_products_list = Product.objects.order_by('product_name')
    context = {'alphabetical_products_list': alphabetical_products_list}
    return render(request, 'products/index.html', context)

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ProductForm()
    return render(request, 'products/detail2.html', {'product': product, 'form' : form})
