from django.contrib import admin
from .models import Post,Category


class postadmin(admin.ModelAdmin):
    list_display=('title','content')
    search_fields=('title','content')
    list_filter=('category','created_at')

admin.site.register(Post,postadmin)
admin.site.register(Category)

# Register your models here.
