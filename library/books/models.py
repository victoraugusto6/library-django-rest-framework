from django.db import models

STATES_BOOKS = (
    (0, 'Novo'),
    (1, 'Usado')
)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    release_year = models.IntegerField()
    state = models.IntegerField(choices=STATES_BOOKS)
    pages = models.IntegerField()
    publish_company = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.release_year}'
