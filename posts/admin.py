from django.contrib import admin
from posts.models import Post


@admin.register(Post)
class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.site_title = 'Blog Test application'
admin.site.site_header = 'Blog Test application'