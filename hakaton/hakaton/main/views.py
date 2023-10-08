from django.shortcuts import render, redirect
from .models import Tiket
from .forms import TiketForm


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TiketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://192.168.1.4:8080/')
        else:
            error = 'Упс, вы что-то неверно заполнили!' \
                    'попробуйте еще раз!'


    form = TiketForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

def registr(request):
    tiket = Tiket.objects.all()
    return render(request, 'main/registr.html', {'title': 'Личный кабинет', 'tikets': tiket})