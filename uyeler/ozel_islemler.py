# -*- coding: utf-8 -*-
from django.core.exceptions import PermissionDenied


class IPKontrolMiddleware(object):

    def process_request(self, request):

        iplistesi = ['192.168.1.1', '127.0.0.1', '0.0.2.35']
        ip = request.META.get('REMOTE_ADDR')

        print "process_request = sorgu, ", ip

        if ip not in iplistesi:
            raise PermissionDenied

        return None


    def process_response(self, request, response):

        print "process_response = yanıt, ", request.path

        return response
