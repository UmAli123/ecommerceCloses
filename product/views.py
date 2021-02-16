from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import ProductForm
from .models import Product
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
@login_required
@csrf_exempt
def product(request):
    data=dict(request.POST)
    if request.method=="POST":
        form =ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form =ProductForm()
        # category=CategoryForm()
        return render(request,"product.html",{'form':form})
    
@login_required
@csrf_exempt    
def allProduct(request):
    category=Product.objects.all()
    return render(request,"all.html",{'Products':category})

class updateproduct(UpdateView):
    login_required = True
    model = Product
    template_name = 'product.html'
    form_class = ProductForm
    success_url = reverse_lazy('index')
    
class Deleteproduct(DeleteView):
    login_required = True
    model = Product
    template_name = 'product1.html'
    form_class = ProductForm
    success_url = reverse_lazy('index')