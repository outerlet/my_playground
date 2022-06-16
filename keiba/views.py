from django.views import View
from django.shortcuts import render

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'keiba/index.html')

index = IndexView.as_view()
