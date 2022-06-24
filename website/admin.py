from django.contrib import admin
from .models import Categories,post
from .models import authorInsight,post_details,contactInfo


# Register your models here.

# Registration for configuration

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('icon_tag','title','url','paragraph')

    search_fields = ('title',)

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title',)
#     list_filter = ('category',)
#     search_fields = ('title',)


admin.site.register(Categories,CategoryAdmin)
admin.site.register(post)
admin.site.register(authorInsight)
# admin.site.register(portfolios)
admin.site.register(post_details)
admin.site.register(contactInfo)

