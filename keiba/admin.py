from django import forms
from django.contrib import admin
from keiba import models


class HorseAdminForm(forms.ModelForm):
    def clean_age(self):
        value = self.cleaned_data['age']
        if value < 0:
            raise forms.ValidationError('年齢は0以上を入力してください')
        return value


class HorseModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'sex')
    ordering = ('age',)
    fields = ('name', 'age', 'sex')
    form = HorseAdminForm


# Register your models here.
admin.site.register(models.Horse, HorseModelAdmin)
admin.site.register(models.Race)
