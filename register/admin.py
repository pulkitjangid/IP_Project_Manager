from django.contrib import admin
from .models import MUser, Room, Message 
# Register your models here.
admin.site.register(Room)
admin.site.register(Message)

@admin.register(MUser)



class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'Student_Name', 'Project_Name', 'Roll_No', 'Description')

