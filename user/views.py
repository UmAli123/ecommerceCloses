from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives,send_mail
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from product.models import Product
from django.views.decorators.csrf import csrf_exempt
from .models import UserCloses
##################################################################
####################index#######################################

def Buyer(request):
    products= Product.objects.all()
    #messages.success(request, f' {username} you are Buyer!!')
    return render(request, 'user/buyer.html', {'title':'the buyer select his own closes','objects':products})





def index(request):
    products= Product.objects.all()
    return render(request, 'user/seller.html',{'title':'index','objects':products})
########################################################################
########### register here #####################################
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) or None
        if form.is_valid():
            username = request.POST.get('username')
            #########################mail####################################
            htmly = get_template('user/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'hello', settings.EMAIL_HOST_USER, request.POST.get('email')
            html_content = htmly.render(d)
            msg = send_mail(subject, html_content, from_email, [to])
            #msg.attach_alternative(html_content, "text/html")
            try:
                msg.send()
            except:
                print("error in sending mail")
            ##################################################################
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form,'title':'reqister here'})

###################################################################################
################login forms###################################################
@csrf_exempt
def Login(request):
    if request.method == 'POST':

        #AuthenticationForm_can_also_be_used__

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request,user)
            messages.success(request, f' wecome {username} !!')
            customer=UserCloses.objects.get(id=user.id)
            print(customer)
            if customer.user_type=='SELLER':
                messages.success(request, f' {username} you are seller!!')
                return redirect('index')
            else:
                products= Product.objects.all()
                messages.success(request, f' {username} you are Buyer!!')
                return render(request, 'user/buyer.html', {'form':form,'title':'the buyer select his own closes','objects':products})
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form,'title':'log in'})
