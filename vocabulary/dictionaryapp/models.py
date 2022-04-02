from django.db import models


class Word(models.Model):
    eng_word = models.CharField(max_length=128)
    rus_word = models.CharField(max_length=128)
    note = models.TextField(blank=True)

    def __str__(self):
        return f'{self.eng_word} - {self.rus_word}'
