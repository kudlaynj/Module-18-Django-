from django.shortcuts import render


# Create your views here.
def task3_1(request):
    title = 'Главная'
    text = ''
    context = {
        'title': title,
        'text': text,
    }
    return render(request,'platform.html', context)


def task3_2(request):
    title = 'Услуги'
    text = ''
    context = {
        'title': title,
        'text': text,
    }
    return render(request,'services.html', context)


def task3_3(request):
    title = 'Методические материалы'
    text = ''
    context = {
        'title': title,
        'text': text,
    }
    return render(request,'methodological_materials.html', context)


def task3_4(request):
    title = 'Корзина'
    text = ''
    context = {
        'title': title,
        'text': text,
    }
    return render(request,'cart.html', context)
