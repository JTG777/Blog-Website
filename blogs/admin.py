from django.contrib import admin
from .models import Post,Comment,Tag,Category,Like

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':['name'],}
    list_display=['name','slug']

class TagAdmin(admin.ModelAdmin):
    # prepopulated_fields={'slug':['name'],}
    list_display=['name','slug']    

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag,TagAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Like)
admin.site.register(Comment)
