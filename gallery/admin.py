from django.contrib import admin
from .models import SliderImage
from adminsortable2.admin import SortableAdminMixin

class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    '''
    Админ-панель для модели SliderImage.
    '''
    list_display = ('title', 'image_preview', 'order')
    ordering = ('order',)

    def image_preview(self, obj):
        if obj.image:
            return '<img src="{}" style="width:100px;height:auto;" />'.format(obj.image.url)
        return 'No image'
    image_preview.allow_tags = True

admin.site.register(SliderImage, SliderImageAdmin)
