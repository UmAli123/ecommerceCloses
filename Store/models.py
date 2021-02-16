from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length = 150)
    logo = models.ImageField(null=True,blank = True)
    last_modification = models.DateField( auto_now=False, auto_now_add=False)
    date_add =models.DateField( auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.name
    
class productStore(models.Model):
    product = models.ForeignKey("product.Product", verbose_name="product", on_delete=models.CASCADE)
    store   = models.ForeignKey("Store.Store", verbose_name="Product store", on_delete=models.CASCADE)