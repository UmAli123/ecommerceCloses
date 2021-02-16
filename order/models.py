from django.db import models
from user.models import UserCloses
# Create your models here.
from django.utils.translation import ugettext_lazy as _
class Order(models.Model):
    customer = models.ForeignKey(UserCloses, verbose_name="Customer", on_delete=models.CASCADE)
    Delivery_name =models.TextField()
    street   =models.TextField()
    address =models.TextField("Address")
    Card_number = models.CharField("Card Number", max_length=19)
    state =models.CharField("State", max_length=50)
    country =models.CharField("country", max_length=50,default="SUDAN")
    payment_method =models.CharField("Payment Method", max_length=50,default="card to card")
    date_purchased =models.DateField( auto_now=True, auto_now_add=False)
    last_modification = models.DateField( auto_now=True, auto_now_add=False)
    # shipping_cost = models.DecimalField("Shipping Cost", max_digits=5, decimal_places=2)
    # shipping_method = models.CharField("Shipping Method", max_length=50)
    status = models.IntegerField("Status",default=0)
    date_finished = models.DateField("Dated Finished", auto_now=True, auto_now_add=False,null=True,blank=True)
    comments      = models.TextField("Comments")
    currency = models.CharField( max_length=5,default="SDG")
# class order1(models.Model):
#     customer = models.ForeignKey(UserCloses, verbose_name="Customer", on_delete=models.CASCADE)
    