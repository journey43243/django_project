from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Companys, User, usersOrders, Product
import uuid

admin.site.register(User)
admin.site.register(usersOrders)
admin.site.register(Product)

@admin.register(Companys)
class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("nameOfCopmany", )} 
    list_per_page = 5
    list_display = ('nameOfCopmany','Descripton')
    list_editable = ('Descripton', )
    search_fields = ('nameOfCopmany', )

    
