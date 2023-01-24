import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views import View

from Api.tasks import handle_csv_file
from Api.models import CSV


class EchoView(View):
    message = None

    def get(self, request):
        return HttpResponse(self.__class__.message)

    def put(self, request):
        self.__class__.message = json.loads(request.body).get("message")
        return HttpResponse(status=200)


class TopView(View):
    def get(self, request):
        field = request.GET.get('field')
        count = request.GET.get('count')

        files = CSV.objects.all()
        for file in files:
            # Как-то крч сортирнуть и сформировать Json
            pass
        response_json = {'mda': 'mda'}
        return JsonResponse(data=response_json)


class UploadView(View):
    def get(self, request):
        return render(request, 'Api/upload.html')

    def post(self, request):
        handle_csv_file(request.FILES["file"]).delay()
        return HttpResponse(status=200)
