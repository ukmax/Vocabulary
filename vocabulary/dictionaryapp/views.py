from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView

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


class WordDetailView(DetailView):
    template_name = 'word.html'
    model = Word
    pk_url_kwarg = 'pk'
    context_object_name = 'word'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        examples = list(Example.objects.filter(word__eng_word=self.object.eng_word).only("eng_example", "rus_example"))
        context['examples'] = examples
        return context


class WordListView(ListView):
    model = Word
    context_object_name = 'all_words'
    template_name = 'index.html'


class WordCreateView(CreateView):
    model = Word
    template_name = 'word_create.html'
    success_url = reverse_lazy('main')
    fields = '__all__'


class WordUpdateView(UpdateView):
    model = Word
    template_name = 'word_create.html'
    success_url = reverse_lazy('main')
    fields = '__all__'


def topwords(request):
    all_words = list(Word.objects.all())
    context = {'all_words': all_words}
    return render(request, 'topwords.html', context=context)

def checkwords(request):
    all_words = list(Word.objects.all())
    context = {'all_words': all_words}
    return render(request, 'checkwords.html', context=context)

def about (request):
    return render(request, 'about.html')
