from django.shortcuts import render, get_object_or_404
from .models import Word, Example


def index(request):
    all_words = list(Word.objects.all())
    examples = []
    for word in all_words:
        example = list(Example.objects.filter(word__eng_word=word.eng_word).only("eng_example", "rus_example"))
        examples.append(example)
    word_with_examples = list(zip(all_words, examples))  # склеиваем слова и примеры для этих слов

    context = {'word_with_examples': word_with_examples}
    return render(request, 'index.html', context=context)


def word_detail(request, pk):
    word_info = get_object_or_404(Word, pk=pk)
    context = {'word': word_info}
    return render(request, 'word.html', context=context)

