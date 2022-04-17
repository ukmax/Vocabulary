from django.test import TestCase
from django.urls import reverse
from .models import Word


class TestWords(TestCase):

    ENG_WORD = 'some English word'
    RUS_WORD = 'некоторое слово по-английски'
    NOTE = 'заметка'
    UPDATED_NOTE = 'обновленная заметка'

    def setUp(self):
        self.word = Word.objects.create(eng_word=self.ENG_WORD, rus_word=self.RUS_WORD, note=self.NOTE)

    def tearDown(self):
        print('выполняем tearDown')

    def test_create_new_word(self):
        self.assertEqual(self.word.eng_word, self.ENG_WORD)
        self.assertEqual(self.word.rus_word, self.RUS_WORD)
        self.assertEqual(self.word.note, self.NOTE)

    def test_update_word_note(self):
        response = self.client.post(
            reverse('word_update', kwargs={'pk': self.word.id}),
            {'eng_word': self.ENG_WORD, 'rus_word': self.RUS_WORD, 'note': self.UPDATED_NOTE}
        )
        self.assertEqual(response.status_code, 302)
        self.word.refresh_from_db()
        self.assertEqual(self.word.note, self.UPDATED_NOTE)

    def test_show_word_on_main(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['all_words'][0], self.word)

