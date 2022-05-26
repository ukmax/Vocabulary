from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

from .models import Word, Example


def index(request):
    all_user_words = list(Word.objects.filter(user__id=request.user.id))
    context = {'all_words': all_user_words}
    print(request.user.username)
    return render(request, 'index.html', context=context)


# def word_detail(request, pk):
#     word = get_object_or_404(Word, pk=pk)
#     examples = list(Example.objects.filter(word__eng_word=word.eng_word).only("eng_example", "rus_example"))
#     context = {'word': word, 'examples': examples}
#     return render(request, 'word.html', context=context)


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


# class WordListView(ListView):
#     model = Word
#     context_object_name = 'all_words'
#     template_name = 'index.html'


class WordCreateView(LoginRequiredMixin, CreateView):

    model = Word
    template_name = 'word_create.html'
    success_url = reverse_lazy('main')
    fields = '__all__'
    # fields = ['eng_word', 'rus_word', 'note']
    # для подстановки user в форму

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class WordUpdateView(UpdateView):
    model = Word
    template_name = 'word_create.html'
    success_url = reverse_lazy('main')
    # fields = '__all__'
    fields = ['eng_word', 'rus_word', 'note']

    # # для подстановки user в форму
    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user
    #     return super().form_valid(form)

def topwords(request):
    all_words = list(Word.objects.raw('SELECT *, COUNT(*) as CNT FROM dictionaryapp_word GROUP BY eng_word ORDER by CNT DESC  LIMIT 20'))
    context = {'all_words': all_words}
    return render(request, 'topwords.html', context=context)


def checkwords(request):
    all_words = list(Word.objects.filter(user__id=request.user.id).order_by('?'))
    # формируем построчно таблицу для вывода
    first_row = all_words[0:4]
    second_row = all_words[5:9]
    third_row = all_words[9:13]
    words_table = [first_row, second_row, third_row]
    context = {'words_table': words_table}
    return render(request, 'checkwords.html', context=context)

def about (request):
    return render(request, 'about.html')


def delete_word(request, pk):
    Word.objects.filter(pk=pk).delete()
    return redirect('main')
