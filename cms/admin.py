from django.contrib import admin

from models import Page


class PageAdmin(admin.ModelAdmin):
    model = Page
    list_display = ('headline', 'parent', 'get_full_slug', 'public')

admin.site.register(Page, PageAdmin)
