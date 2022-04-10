from django.shortcuts import render, get_object_or_404
from .models import Word, Example


def index(request):
    all_words = list(Word.objects.all())
    context = {'all_words': all_words}
    return render(request, 'index.html', context=context)


def word_detail(request, pk):
    word = get_object_or_404(Word, pk=pk)
    examples = list(Example.objects.filter(word__eng_word=word.eng_word).only("eng_example", "rus_example"))
    context = {'word': word, 'examples': examples}
    return render(request, 'word.html', context=context)

