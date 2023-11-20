from django.contrib import admin

from app.models import Comments, Post, Profile, Tag, WebsiteMeta

# Register your models here.
class PostAdmin(admin.ModelAdmin):
  list_display = ('title','last_updated','nombre_completo', 'likes_total')
  list_filter = ('last_updated',)
  
  search_fields = ('title',)
  search_help_text = 'Buscar por titulo' 
  
  date_hierarchy = 'last_updated'
  
  @staticmethod
  def nombre_completo(obj):
    return f'{obj.author.first_name} {obj.author.last_name} ' 
  
  @staticmethod
  def likes_total(obj):
    return f'{obj.likes.count()}' 
     
class TagAdmin(admin.ModelAdmin):
  pass
class CommentsAdmin(admin.ModelAdmin):
  list_display = ('name', 'email','date')
  sortable_by = ('name','email','date')
  fields = ('name', 'content','date','email', 'parent')
  readonly_fields=('name', 'content','date','email','parent')
  
class WebsitemetaAdmin(admin.ModelAdmin):
  pass  
  

admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Profile)
admin.site.register(WebsiteMeta,WebsitemetaAdmin)