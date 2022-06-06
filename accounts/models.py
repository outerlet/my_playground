from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Publisher(models.Model):
    """出版社モデル"""
    class Meta:
        db_table = 'publishers'

    name = models.CharField(verbose_name='出版社名', max_length=255, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    """著者モデル"""
    class Meta:
        db_table = 'authors'

    name = models.CharField(verbose_name='著者名', max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """本モデル"""
    class Meta:
        db_table = 'books'

    publisher = models.ForeignKey(Publisher, verbose_name='出版社', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=255, unique=True)
    price = models.IntegerField(verbose_name='価格', null=True, blank=True)
    authors = models.ManyToManyField(Author, verbose_name='著者名')
    description = models.URLField(verbose_name='商品ページ', null=True, blank=True)

    def __str__(self):
        return f'{self.title}（{self.publisher}） - {self.price}円,'


class BookStock(models.Model):
    """在庫モデル"""
    class Meta:
        db_table = 'book_stocks'

    book = models.OneToOneField(Book, verbose_name='本', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='在庫数', default=0)
