from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=50)
    date_add    = models.DateField( auto_now=True, auto_now_add=False) 
    laste_Modified =models.DateField( auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.category_name
class subCategory(models.Model):
    sub_name = models.CharField(max_length=50)
    Category_idea = models.ForeignKey("Category.Category", on_delete=models.CASCADE)
    def __str__(self):
        return self.sub_name
    
    