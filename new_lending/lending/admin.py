from django.contrib import admin
from .models import Companys,Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('productModel','Maker','stock','cost')
    list_display_links = ('productModel','Maker')
    list_editable = ('stock','cost')
    list_per_page = 5
    search_fields = ('productModel',)
    list_filter = ('stock', 'Maker__nameOfCopmany')
    actions = ('set_stock', 'delete_stock')

    @admin.action(description= "Add to stock")
    def set_stock(self, request,queryset):
        count = queryset.update(stock = Product.Status.inStock)
        self.message_user(request,f"{count} товаров добавлено в наличие")

    @admin.action(description= "Delete from stock")
    def delete_stock(self, request,queryset):
        count = queryset.update(stock = Product.Status.outStock)
        self.message_user(request,f"{count} товаров убрано из наличия")

@admin.register(Companys)
class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("nameOfCopmany", )} 
    list_per_page = 5
    list_display = ('nameOfCopmany','Descripton')
    list_editable = ('Descripton', )
    search_fields = ('nameOfCopmany', )

