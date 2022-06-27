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
        return f'name = {self.name}, age = {self.age}, sex = {self.sex_text()}'
