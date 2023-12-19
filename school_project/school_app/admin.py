
# from django.contrib import admin
# from .models import Form, department
# from .models import materials
# from .views import course
#
# admin.site.register(Form)
# admin.site.register(materials)
# admin.site.register(department)
# admin.site.register(course)
# # Register your models here.
from django.contrib import admin
from .models import Form


admin.site.register(Form)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'dob', 'gender', 'address', 'mail_id','age', 'department', 'courses', 'purpose','materials', 'phone_number']