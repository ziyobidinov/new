from django.views.generic import View
from django.shortcuts import render

from common.models import Gallery


class HomeView(View):
    def get(self, request):
        gallery = Gallery.objects.all()

        context = {
            "galleries": gallery,
        }

        return render(request, "index.html", context)
