from django.db import models

# Create your models here.
class Horse(models.Model):
    class Meta:
        db_table = 'horse'
    
    name = models.CharField(verbose_name='名前', max_length=255, unique=False, null=False)
