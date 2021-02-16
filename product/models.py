from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 150)
    model= models.TextField()
    quntity =models.IntegerField()
    price   = models.DecimalField(max_digits=10,decimal_places=2)
    date_add =models.DateField( auto_now=True, auto_now_add=False)
    last_modification = models.DateField( auto_now=False, auto_now_add=False)
    weight =models.DecimalField(max_digits=5, decimal_places=2)
    status = models.IntegerField(null=True)
    sub_category =models.ForeignKey("Category.subCategory", on_delete=models.CASCADE)
    image   = models.ImageField(null=True,blank = True)
    RecieveCard_number = models.CharField("Card Number", max_length=19)
    
    def __str__(self):
        return self.name
# class productImage(models.Model):
#     product = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    