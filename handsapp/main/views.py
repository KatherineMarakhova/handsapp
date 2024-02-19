from django.shortcuts import render

# Create your views here.


def index(response):
    data = {
        'title': 'Главная страница',
        'values': ['tam', 'tut', 'syam'],
        'somelist': {
            'one': '1000',
            'two': '200',
            'three': '3'
        }
    }
    return render(response, 'main/index.html', data)


def about(response):
    return render(response, 'main/about.html')
