from django.shortcuts import render


# Create your views here.
def task3_1(request):
    return render(request, 'platform.html')


def task3_2(request):
    serv = {
        'serv': ['Консультация логопеда', 'Консультация нейропсихолога', 'Консультация психолога']
    }
    return render(request, 'services.html', serv)


def task3_3(request):
    content = {
        'content': ['Набор логопедических зондов', 'Кубики Кооса', 'Балансировочная доска'],
    }
    return render(request, 'methodological_materials.html', content)


def task3_4(request):
    return render(request, 'cart.html')


def menu(request):
    return render(request, 'menu.html')

