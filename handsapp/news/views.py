from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Articles
from .forms import ArticlesForm


def news_home(request):
    # news = Articles.objects.all()
    news = Articles.objects.order_by('-date')
    return render(request, 'news/newshome.html', {'news': news})


class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'news/details.html'
    context_object_name = 'article'


def add_new(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newshomepage')
        else:
            error = 'Форма заполнена неверно'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/addnew.html', data)


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/addnew.html'
    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/delete-news.html'
    success_url = '/news'
