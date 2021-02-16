from django.shortcuts import render
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
# Create your views here.
from .models import Order
from product.models import Product
from .forms import OrderForm

from django.shortcuts import render,redirect
import random
import datetime
from django.http.response import JsonResponse
from django.db.models import Sum
from morsal import Transactions_body
from morsal.views import Morsal_APIs
from morsal.PinBlock import PinBlock
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# Create your views here.
from django.contrib import messages
@csrf_exempt
class CardToCard():
    def post(self,data):
      
        morsal =Morsal_APIs()
        mastercard_body=[]
    
        TWK = morsal.getWorking_Key(Transactions_body.Working_Key)
        pinb =PinBlock(data['PIN'],data['PAN'],TWK,Transactions_body.TMK)
        Transactions_body.Card_to_Card['systemTraceAuditNumber']=(random.randrange(0, 9998)+1)
        Transactions_body.Card_to_Card['tranDateTime']=str(datetime.datetime.now())
        Transactions_body.Card_to_Card['PAN']=data['PAN']
        Transactions_body.Card_to_Card['PIN']= pinb.encrypted_pin_block()
        Transactions_body.Card_to_Card['expDate']=data['expDate']
        Transactions_body.Card_to_Card['toCard']=data['toCard']
        Transactions_body.Card_to_Card['tranAmount']=data['tranAmount']
        balance = morsal.Card_to_Card(Transactions_body.Card_to_Card)
        if balance.status_code == 200:
            context = {
            
            'Result': balance.json()['additionalAmount']
            }
            return context
        else:
            context = {
            
            'Result': balance.json()
            }
            return context


def Payment(request,id):
    data=dict(request.POST)
    if request.method=="POST":
        objects =Product.objects.get(id=id)
        payment={"PAN":data['Card_number'],"PIN":data['PIN'],"expDate":data['expDate'],"toCard":objects.RecieveCard_number,"tranAmount":objects.price}
        if objects.quntity==0:
            messages.success(request, f'The Product Empty quantity,')
        else:
            form =OrderForm(data)
            if form.is_valid():
                balance= CardToCard()
                result =balance.post(payment)
               
                if result['responseCode']==0:
                    messages.success(request, f'The payment was successfully done!!')
                else:
                    messages.success(request,result)
                return redirect('buyer')
            else:
                messages.success(request, f'data Entered error . please try a gain.')
                return redirect('buyer')
                
    else:
        objects =Product.objects.get(id=id)
        return render(request,"payment.html",{'product':objects,'id':id})


# class Payment(CreateView):
#     login_required = True
#     model = Order
#     template_name = 'payment.html'
#     # 
#     success_url = reverse_lazy('buyer')
#     # def get(self,request,id,*args):
#     #     return super(Payment, self).get(request, *args, kwargs={'id':id})
class Updateoder(UpdateView):
    login_required = True
    model = Order
    template_name = 'payment.html'
    
    success_url = reverse_lazy('buyer')
class Deletepayment(DeleteView):
    login_required = True
    model = Order
    template_name = 'payment1.html'
    success_url = reverse_lazy('buyer')