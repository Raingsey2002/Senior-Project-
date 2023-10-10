from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Member
from .models import Category, Website, Rating, CommentandRating

# Register your models here.



admin.site.register(Member,UserAdmin)
admin.site.register(Category)
admin.site.register(Website)
admin.site.register(Rating)
admin.site.register(CommentandRating)
fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal Info', {'fields':('first_name','last_name','email','gender','dateofbirth','image')})
UserAdmin.fieldsets = tuple(fields)
