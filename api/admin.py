from django.contrib import admin
from . import models

class GroupAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass

class NoticeAdmin(admin.ModelAdmin):
    pass

class ProgramAdmin(admin.ModelAdmin):
    pass

class LinkAdmin(admin.ModelAdmin):
    pass

class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Group, GroupAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Notice, NoticeAdmin)
admin.site.register(models.Program, ProgramAdmin)
admin.site.register(models.Link, LinkAdmin)
admin.site.register(models.Image, ImageAdmin)
