from django.contrib import admin
from news.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','created_at','is_published')
    list_display_links = ('id','title')
    list_filter = ('author',)
    list_editable = ('is_published',)
    search_fields = ('title','content','summary')
    list_per_page = 25
# Register your models here.
admin.site.register(Post, PostAdmin)