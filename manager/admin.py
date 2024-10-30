from django.contrib import admin
from .models import videos,inventory
# Register your models here.
class videoadmin(admin.ModelAdmin):
    List = ["username","videoname","videolink"]

class inventoryadmin(admin.ModelAdmin):
    List = ["username","item","quan"]

admin.site.register(videos,videoadmin)
admin.site.register(inventory,inventoryadmin)