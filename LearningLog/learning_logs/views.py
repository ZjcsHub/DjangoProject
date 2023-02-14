from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from .models import Topoc
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.

class IndexView(View):
    def get(self,request):
        return render(request,'index.html')


class TopicView(View):
    def get(self,request):
        """显示所有主题"""
        topic = Topoc.objects.order_by('date_added')
        content = {'topics':topic}
        return render(request,'topics.html',content)

class TopicDetailView(View):
    def get(self,request,topic_id):
        topic = Topoc.objects.get(id=topic_id)
        entries = topic.entry_set.order_by('-date_added')
        context = {'topic':topic,'entries':entries}
        return render(request,'topic.html',context)

@method_decorator(csrf_exempt, name='dispatch')
class ChatGPTView(View):
    def get(self,request):
        return render(request,'chatGPT.html')

    def post(self,request):
        q = request.POST.get('q')

        url = 'https://api.openai.com/v1/completions'
        token = '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'
        header = {'Authorization':f'Bearer {token}'}


        data = {
            'prompt':q,
            'model':'text-davinci-003',
            'max_tokens':4000
        }
        r = requests.post(url,json=data,headers=header)
        j_data = r.json()
        choices = j_data.get('choices',[])
        text_lists = []
        for c_dic in choices:
            text_lists.append(c_dic['text'])

        return render(request,'chatGPT.html',{'content': text_lists})