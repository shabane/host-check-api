from django.shortcuts import render
from rest_framework import views
from django.http import HttpResponse
from . import core
from rest_framework.response import Response


class CheckTCP(views.APIView):
    def get(self, request):
        if request.GET.get('host') and request.GET.get('port'):
            __host = request.GET['host']
            __port = request.GET['port']
            _ = core.is_tcp_open(__host, __port)
            return Response({
                'result': _,
                'node': '...'
            })