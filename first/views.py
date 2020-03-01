from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Article


def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'first/list.html', {'latest_articles_list': latest_articles_list})


def show(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return Http404('Article not found!')
    comments = article.comment_set.order_by('-id')[:5]

    return render(request, 'first/show.html', {'article': article, 'comments': comments})


def comment(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return Http404('Article not found!')

    article.comment_set.create(author=request.POST['author'], comment=request.POST['comment'])

    return HttpResponseRedirect(reverse('first:show', args=(article.id,)))
