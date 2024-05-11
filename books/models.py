from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    rating = models.IntegerField()
    picture = models.ImageField(default=None, null=True, blank=True, upload_to='books')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    picture = models.ImageField(default=None, null=True, blank=True, upload_to='authors')
    books = models.ManyToManyField(Book)

    class Meta:
        ordering = ['name']
    def __str__(self):
        return f'{self.name}  {self.surname}'
