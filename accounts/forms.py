from django import forms
from accounts.models import Publisher


class LoginForm(forms.Form):
    username = forms.CharField(label='ユーザー名', max_length=255)
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 3:
            raise forms.ValidationError(
                message='%(min_length)s文字以上で入力してください',
                code='invalid',
                params={'min_length': 3}
            )
        return username

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if len(username) > 10 and len(password) > 10:
            raise forms.ValidationError('正しいユーザー名とパスワードの組み合わせを入れてください')


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ('name',)
