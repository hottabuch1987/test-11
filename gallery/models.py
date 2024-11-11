from django.db import models
from filer.fields.image import FilerImageField


class SliderImage(models.Model):
    '''
    Модель для хранения изображений в слайдере.
    '''
    image = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255, null=True, blank=True)
    order = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        ordering = ('order',)  # Сортировка по порядку

    def __str__(self):
        if self.title:
            return self.title
        return f"Слайд {self.id}"
