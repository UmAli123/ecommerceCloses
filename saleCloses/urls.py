"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from user import views as user_view
from django.contrib.auth import views as auth
from django.conf.urls.static import static
from django.conf import settings
from .router import router
from rest_framework.authtoken import views
from Category.views import createCatgory,allcategory
from product.views import product,allProduct,updateproduct,Deleteproduct
from Store.views import Store,ProductStore,allStore
admin.site.site_header = 'E commerce for sailing closes'
from order.views import Payment
urlpatterns = [

    path('admin/', admin.site.urls),
    path('category/',createCatgory,name='category'),
    path('allcategory/',allcategory,name='category-all'),
    #allStore
    path('Product/',product,name='product'),
    path('Product-update/<int:pk>/',updateproduct.as_view(),name='product-update'),
    path('Product-delete/<int:pk>/',Deleteproduct.as_view(),name='product-delete'),
    
    path('allproducts/',allProduct,name='product-all'),
    
    path('store/',Store,name='store'),
    path('payment/<int:id>/',Payment,name='payment'),
    
    path('allstore/',allStore,name='store-all'),
    
    path('ProductStore/',ProductStore,name='ProductStore'),
    
    
    
    ######### api path ##########################

    path('api/',include(router.urls)),
    path('api-token-auth/',views.obtain_auth_token,name='api-tokn-auth'),

    #####user related path##########################
    path('',include('user.urls')),
    path('login/',user_view.Login,name='login'),
    path('logout/',auth.LogoutView.as_view(template_name='user/index.html'),name='logout'),
    path('register/',user_view.register,name='register'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
