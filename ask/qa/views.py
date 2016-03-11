from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from qa.models import Question, Answer


def test(request):
    post = Question.objects.all().order_by('-added_at')

    paginator = Paginator(post, 1)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'post.html', {'post': post, 'contacts': contacts, 'page': page})


def popular(request):
    post = Question.objects.all().order_by('-rating')

    paginator = Paginator(post, 1)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'popular.html', {'post': post, 'contacts': contacts, 'page': page})

def question(request, post_id):
    qu = get_object_or_404(Question, pk=post_id)
    an = Answer.objects.all()
    return render(request, 'question.html', {'qu': qu, 'an': an})
