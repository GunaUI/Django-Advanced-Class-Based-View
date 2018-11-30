from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView

# Create your views here.
def index(request):
    return render(request,'index.html')

class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')

class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context