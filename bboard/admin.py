from django.contrib import admin

# Register your models here.

from .models import Bb

from .models import Rubric
admin.site.register(Rubric)


class BbAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "price", "published", "rubric")
    list_display_links = ("title", "content", "price")
    search_fields = ("title", "content",)


admin.site.register(Bb, BbAdmin)
