from django.shortcuts import render
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

