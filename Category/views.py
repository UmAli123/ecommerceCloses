from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import subCategoryForms,CategoryForm
from django.http import JsonResponse
from Category.models import Category,subCategory
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
@login_required
@csrf_exempt
def createCatgory(request):
    data=dict(request.POST)
    if request.method=="POST":
        form =subCategoryForms(request.POST)
        category=CategoryForm(request.POST)
        print(form.is_valid())
        print(category.is_valid())
        if form.is_valid() and category.is_valid():
            category.save()
            obj=Category.objects.filter(category_name=data['category_name'][0],laste_Modified=data['laste_Modified'][0])[0]
            target=subCategory(sub_name=data['sub_name'][0],Category_idea=obj)
            target.save()            
            # form.save()
        return redirect('index')
    else:
        form =subCategoryForms()
        category=CategoryForm()
        return render(request,"Category.html",{"Category":category,'form':form})
    
@login_required
@csrf_exempt    
def allcategory(request):
    category=subCategory.objects.all()
    return render(request,"allcategory.html",{'categories':category})


class updateCategory(UpdateView):
    login_required = True
    template_name = 'Category.html'
    form_class = CategoryForm
    success_url = '/index/'
class updateSubCategory(UpdateView):
    login_required = True
    template_name = 'Category.html'
    form_class = subCategoryForms
    success_url = '/index/'
class CreateCategory(CreateView):
    login_required = True
    template_name = 'Category.html'
    form_class = CategoryForm
    success_url = '/index/'
# class CreateSubCategory(CreateView):
#     login_required = True
#     template_name = 'Category.html'
#     form_class = subCategoryForms
#     success_url = '/index/'
    
class DeleteCategory(DeleteView):
    login_required = True
    template_name = 'Category.html'
    form_class = CategoryForm
    success_url = '/index/'
class DeleteSubCategory(DeleteView):
    login_required = True
    template_name = 'Category.html'
    form_class = subCategoryForms
    success_url = '/index/'