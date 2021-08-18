from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'category', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    # search_fields = ('title', 'content')
    list_editable = ("is_published",)
    list_filter = ('is_published', 'category')
    # fields = ('title', 'category', 'content', 'photo', 'get_photo', 'views', 'created_at', 'updated_at', 'is_published',)
    readonly_fields = ('created_at', 'updated_at', 'get_photo', 'views')
    save_on_top = True

    fieldsets = (
        (None, {
            'fields': ('title', 'category', 'content', 'photo', 'get_photo','is_published',)
        }),
        ('Readonly dashter', {
            'fields': ('views', 'created_at', 'updated_at',),
        }),
    )


    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75px">')
        else:
            return "Nkar chka."

    get_photo.short_description = 'Nkar'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    # search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Norutyunneri karavarum'
admin.site.site_header = 'Norutyunneri karavarum'
