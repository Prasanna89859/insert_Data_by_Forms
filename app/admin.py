from django.contrib import admin
from app.models import *

# Register your models here.
class customizewebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url']
    #list_display_links=['url']
    #list_editable=['url']
    search_fields=['name']
    #list_per_page=[0]
    list_filter=('name',)


admin.site.register(Topic)
admin.site.register(Webpage,customizewebpage)


admin.site.register(AccessRecord)

