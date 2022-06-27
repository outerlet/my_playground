from django.views import View
from django.shortcuts import render
import keiba

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        horse_list = \
            [ {'name': h.name, 'age': h.age, 'sex': h.sex_text()} for h in keiba.models.Horse.objects.all() ]

        context = {
            'horse_list': horse_list
        }

        return render(request, 'keiba/index.html', context)

index = IndexView.as_view()
