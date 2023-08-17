from django.shortcuts import render
from rest_framework import views
from django.http import HttpResponse
from . import core
from rest_framework.response import Response
from checkhost_prj.settings import NODE

class CheckTCP(views.APIView):
    def get(self, request):
        if request.GET.get('host') and request.GET.get('port'):
            __timeout = request.GET.get('timeout') if request.GET.get('timeout') else '5'
            __timeout = int(__timeout) if __timeout.isdigit() else core.err("timeout should be integer")
            __host = request.GET['host']
            __port = request.GET['port']
            _ = core.is_tcp_open(__host, __port, __timeout)
            return Response({
                'result': {
                    'ok': _,
                },
                'node': NODE
            })
