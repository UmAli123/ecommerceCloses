from django.contrib import admin
from Category.models import Category, subCategory
# Register your models here.
admin.site.register(Category)

admin.site.register(subCategory)
