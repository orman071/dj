from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from qa.models import Question, Answer


def test(request, pk):
    post = Question.objects.all()
    post.order_by('-id')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(post, limit)
    page = paginator.page(page)
    return render(request, 'post.html', {'post': post, 'paginator': paginator, 'page': page})


def popular(request):
    pop = Question.objects.all().filter('-rating')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(pop, limit)
    page = paginator.page(page)
    return render(request, 'post.html', {'post': pop, 'paginator': paginator, 'page': page})


def question(request, id):
    qu = get_object_or_404(Question, pk=id)
    an = Answer.objects.all()
    return render(request, 'question.html', {'qu': qu, 'an': an})
