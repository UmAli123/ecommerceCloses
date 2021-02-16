
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import StoreForm,productStoreForm
from Store.models import Store,productStore
@login_required
@csrf_exempt
def Store(request):
    if request.method=="POST":
        form =StoreForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form =StoreForm()
        # objects=Store.objects.all()
        i=2
        return render(request,"Store.html",{'form':form,'i':i})
def ProductStore(request):
    if request.method=="POST":
        form =productStoreForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form =productStoreForm()
        # objects=productStore.objects.all()
        i=1
        return render(request,"Store.html",{'form':form,'i':i})
    
def allStore(request):
    category=productStore.objects.all()
    return render(request,"allstore.html",{'Products':category})