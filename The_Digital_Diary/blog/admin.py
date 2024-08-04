from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    #pass
    list_display = ('title', 'created_at')
class PostAdminold(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
admin.site.register(Post, PostAdmin)
admin.site.register(Post1, PostAdminold)
admin.site.register(Comment)