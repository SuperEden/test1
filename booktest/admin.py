from django.contrib import admin
from models import *

class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 2


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']
    list_filter = ['id']
    search_fields = ['btitle']
    list_per_page = 3

    inlines = [HeroInfoInline]

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hcontent', 'hbook']

# Register your models here.
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
