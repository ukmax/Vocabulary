from django.shortcuts import render
from .models import Word


def index(request):
    all_words = Word.objects.all()
    print(all_words)
    context = {'all_words': all_words}

    return render(request, 'index.html', context=context)
