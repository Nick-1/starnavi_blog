from django.shortcuts import render
from django.views import View


class StartPageView(View):

    def get(self, request):
        return render(request, 'start_page.html')