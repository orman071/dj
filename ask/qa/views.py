from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from qa.models import Question


def test(request, pk):



