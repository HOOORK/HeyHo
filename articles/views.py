from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
from django.http import HttpResponse


def home(request):
    """Главная страница с приветствием и ссылкой на статьи"""
    return render(request, 'articles/home.html')


def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'articles/article_list.html', {'articles': articles})


@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'articles/article_form.html', {'form': form})


@login_required
def article_edit(request, id):
    article = get_object_or_404(Article, id=id)

    # Проверяем, что пользователь - автор статьи
    if article.author != request.user:
        return redirect('article_list')

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm(instance=article)

    return render(request, 'articles/article_form.html', {'form': form})