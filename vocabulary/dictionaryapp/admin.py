from django.contrib import admin

# Register your models here.
from .models import Word, Example

admin.site.register(Word)
admin.site.register(Example)
