from django.contrib import admin
from .models import Category, Post, Tag


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'imgurl')
    list_display_links = ('name', )


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'pub_time', 'last_mod_time', 'views')
    list_display_links = ('title', )
    ordering = ('-pub_time', )
    list_filter = ('category', 'status')
    date_hierarchy = 'pub_time'
    fields = ('title', ('category', 'status', 'comment_status'), 'tags', 'pub_time', 'body')
    filter_horizontal = ('tags',)  # 让manytomany表更直白的操作数据


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
