import datetime

from django.db import models
from django.utils import timezone



class Quote(models.Model):
    quote_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.quote_text


class Author(models.Model):
    Quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    author_text = models.CharField(max_length=200)
    def __str__(self):
        return self.author_text
