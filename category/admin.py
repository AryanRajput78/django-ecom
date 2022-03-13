from django.contrib import admin
from . models import Category
# Register your models here.

# it'll autofill slug same name as category
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name','slug')
    
admin.site.register(Category, CategoryAdmin)