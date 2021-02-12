from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .utils import nlp

import re
import time

# Create your views here.
def home(request):
    return render(request, "main/home.html", {})


def about(request):
    return render(request, "main/about.html", {})


def generate(request):
    context = {}
    if request.method == "POST":
        passage = re.sub('\[\w+\]', '', request.POST.get('passage'))

        # start = time.time()
        questions = nlp(passage)[:3]
        # end = time.time()

        context = {
            'passage': passage,
            'questions': questions,
            # 'time': round(end - start, 2),
            'num_questions': len(questions)
        }
    return render(request, "main/generate.html", context)
