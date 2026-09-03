from django.contrib import admin
from .models import Post ,Comment
# Register your models here.
# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title' , 'author' , 'status' ,'publish' , 'created' , 'updated']
    list_filter = ['status' , 'created' , 'publish' , 'author']
    search_fields = ['title' , 'body']
    ordering = ['status' , 'publish']
    # prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    show_facets = admin.ShowFacets.NEVER

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name' ,'email' ,'active']
    list_filter = ['active' ]
    raw_id_fields = ['post']

admin.site.register(Comment,CommentAdmin)