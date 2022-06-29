from tabnanny import verbose
from django.db import models
from enum import Enum

class Sex(Enum):
    MALE = 'M'
    FEMALE = 'F'

# Create your models here.
class Horse(models.Model):
    class Meta:
        db_table = 'horses'
    
    name = models.CharField(verbose_name='名前', max_length=255, unique=False, null=False)
    age = models.IntegerField(verbose_name='年齢', unique=False, null=False)
    sex = models.CharField(verbose_name='性別', max_length=1, unique=False, null=False)

    def sex_text(self):
        if self.sex == Sex.MALE.value:
            return '牡'
        else:
            return '牝'

    def __str__(self):
        return f'馬名: {self.name}, 年齢: {self.age}, 性別: {self.sex_text()}'

class Race(models.Model):
    class Meta:
        db_table = 'races'

    name = models.CharField(verbose_name='レース名', max_length=255, unique=True, null=False)
    grade = models.CharField(verbose_name='格', max_length=10, unique=False, null=True)
    terms = models.CharField(verbose_name='条件', max_length=255, null=True)
