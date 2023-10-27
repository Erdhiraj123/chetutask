from django.contrib import admin
from .models import Users1,CustomUser



class UserAdmin(admin.ModelAdmin):
    list_display=['name','email','password']

class Userforfmadmin(admin.ModelAdmin):
    list_display=['username','first_name','last_name','email','status']




# Register the models with their respective admin classes
admin.site.register(Users1,UserAdmin)
admin.site.register(CustomUser,Userforfmadmin)


