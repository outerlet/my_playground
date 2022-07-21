from django.views import View
from django.shortcuts import render
from keiba import models, forms


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return self.show_index(request, forms.HorseForm())

    def post(self, request, *args, **kwargs):
        form = forms.HorseForm(request.POST)

        if form.is_valid():
            form.save()
            next_form = forms.HorseForm()
        else:
            next_form = form

        return self.show_index(request, next_form)

    def show_index(self, request, form):
        horse_list = \
            [ {'name': h.name, 'age': h.age, 'sex': h.sex_text()} for h in models.Horse.objects.order_by('age', 'name',) ]

        context = {
            'horse_list': horse_list,
            'form': form,
        }

        return render(request, 'keiba/index.html', context)


class HorsesView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'horses': models.Horse.objects.order_by('age'),
        }

        return render(request, 'keiba/horses.html', context)


index = IndexView.as_view()
horses = HorsesView.as_view()
