from django.contrib import admin
from .models import Companys,Product
#import rangefilter.filter

class ProductFilter(admin.ListFilter):
    title = 'Cost'
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('productModel','Maker','stock','cost')
    list_display_links = ('productModel','Maker')
    list_editable = ('stock','cost')
    list_per_page = 5
    search_fields = ['productModel']
    list_filter = ['stock', 'Maker__nameOfCopmany']

@admin.register(Companys)
class CompanyAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ('nameOfCopmany','Descripton')
    list_editable = ('Descripton', )

