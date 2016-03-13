from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from qa.models import Question, Answer
from qa.forms import AnswerForm, AskForm


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

    paginator = Paginator(post, 10)
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
    an = Question.objects.all()


    return render(request, 'question.html', {'qu': qu, 'an': an})


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect('question' )
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form})

def ans(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = AnswerForm()
    return render(request, 'ans.html', {'form': form})