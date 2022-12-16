# 中间件
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class BlockIPSMiddleware(MiddlewareMixin):
    EXCLUDE_IPS = ['172.16.179.152']

    def process_view(self,request,view_func,*view_arg,**view_kwargs):
        '''视图函数调用'''
        user_ip = request.META["REMOTE_ADDR"]
        print("process")
        if user_ip in BlockIPSMiddleware.EXCLUDE_IPS:
            return HttpResponse('<h1>Forbidden</h1>')



class TestMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        '''初始化函数，第一次调用之后，后续不再调用'''
        super().__init__(get_response)
        print("----init-----")

    def process_request(self,request):
        '''产生request对象之后'''
        print("----process_request-----")

    def process_view(self,request,view_func,*view_arg,**view_kwargs):
        '''url 匹配之后，视图函数调用之前调用'''
        print("------process_view------")

    def process_response(self,request,response):
        '''视图函数调用之后，内容返回浏览器之前'''
        print("-------process_response-------")
        return response

    def process_exception(self,request,exception):
        '''视图函数发生异常时调用'''
        print("----process_exception---")

