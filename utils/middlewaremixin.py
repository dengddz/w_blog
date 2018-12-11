# encoding: utf-8
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from backweb.models import MyUser


class LoginStatusMiddleware(MiddlewareMixin):
    
    def process_request(self, request):
        if request.path in ['/backweb/login/','/backweb/register/']:
            return None

        user_id = request.session.get('user_id')
        if user_id:
            user = MyUser.objects.get(pk=user_id)
            request.user = user
            return None
        else:
            return HttpResponseRedirect('/backweb/login/')

    def process_response(self, request, response):
        return response


