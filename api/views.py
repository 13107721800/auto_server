from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
# @method_decorator(csrf_exempt, name='dispatch')
# class Asset(View):
#     def get(self, request):
#         print('get')
#         host_list = [i for i in range(1, 100)]
#         return JsonResponse(host_list, safe=False)
#
#     def post(self, request):
#         print('post')
#         ret = json.loads(request.body.decode('utf-8'))
#         return HttpResponse('接收到了')

from rest_framework.views import APIView
from rest_framework.response import Response


class Asset(APIView):

    def post(self, request):
        print('post')
        response = {'status': True, 'hostname': None, 'error': None}
        if request.method == 'POST':
            print(request.body)
        else:
            # 要从数据库中获取的主机名
            return ['localhost.localdomain']
        return HttpResponse('ok')
