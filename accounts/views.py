from gettext import install
from django.shortcuts import render
from django.contrib import messages
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.template.response import TemplateResponse
from . import models, forms


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        messages.info(request, '初めのペエジです。', extra_tags='sample')
        context = {
            'message': 'This is index view',
        }
        return TemplateResponse(request, 'accounts/index.html', context)


class BooksView(View):
    def get(self, request, *args, **kwargs):
        book_list = models.Book.objects.filter(publisher__name__in=['技術評論社', '秀和システム'])
        return render(request, 'accounts/book_list.html', {'book_list': book_list})


class AnotherView(TemplateView):
    template_name = 'accounts/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Hello, world.'
        return context


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "accounts/login.html", {'form': forms.LoginForm()})

    def post(self, request, *args, **kwargs):
        form = forms.LoginForm(request.POST)
        is_valid = form.is_valid()
        print(f"username = {form.cleaned_data.get('username')}, password = {form.cleaned_data['password']}, is_valid = {is_valid}")
        return render(request, "accounts/login.html", {'form': form})


class PublisherView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "accounts/publisher.html",
            {'form': forms.PublisherForm()}
        )

    def post(self, request, *args, **kwargs):
        form = forms.PublisherForm(request.POST)
        is_valid = form.is_valid()
        if is_valid:
            form.save()
            return render(request, "accounts/publisher.html", {'form': form})
        else:
            return render(request, "accounts/publisher.html", {'form': form})


index = IndexView.as_view()
books = BooksView.as_view()
another = AnotherView.as_view()
login = LoginView.as_view()
publisher = PublisherView.as_view()
