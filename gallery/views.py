from django.shortcuts import render
from .models import SliderImage


def slider_view(request):
    '''
    Представление для отображения слайдера.
    '''
    images = SliderImage.objects.all()
    context = {'images': images, 'title': 'Главная страница'}
    return render(request, 'gallery/slider.html', context)

