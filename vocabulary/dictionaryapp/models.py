from django.db import models

from myauth.models import MyUser


class Word(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    eng_word = models.CharField(max_length=128)
    rus_word = models.CharField(max_length=128)
    note = models.TextField(blank=True)

    def __str__(self):
        # return f'{self.eng_word} - {self.rus_word}'
        return f'{self.eng_word}'


class Example(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    eng_example = models.CharField(max_length=256)
    rus_example = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.eng_example} - {self.rus_example}'
