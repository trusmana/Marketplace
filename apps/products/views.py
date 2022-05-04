from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.accounts.models import AccountsUser as user
from .models import Products
from .forms import ProductsForm

@login_required
def list_products(request):
    products = Products.objects.all()
    return render(request,'member/home-member.html',{'products':products})

@login_required
def add_products(request):
    user = request.user
    if request.method == 'POST':
        form = ProductsForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.cu = user
            product.save()
            messages.add_message(request, messages.INFO,'Products berhasil Di simpan')
    else:
        form = ProductsForm()
    return render(request,'products/add_products.html',{'form':form})
