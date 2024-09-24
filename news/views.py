from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

@login_required
def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'news/article_list.html', {'articles': articles})

@login_required
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'news/article_detail.html', {'article': article})

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'news/create_article.html', {'form': form})
