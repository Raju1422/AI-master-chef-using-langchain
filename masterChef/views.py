from django.shortcuts import render,redirect
from django.views import View
from .forms import ReceipeForm
from .langchain import askMasterChef
class Home(View):
    def get(self,request):
        ai_receipe = request.session.get('ai_receipe','')
        form = ReceipeForm()
        return render(request,"home.html",{"form":form,"ai_receipe":ai_receipe})
    
    def post(self,request):
        form = ReceipeForm(request.POST)
        if form.is_valid():
            receipe_message =form.cleaned_data['receipe_message']
            ai_response= askMasterChef(receipe_message)
            request.session['ai_receipe']=ai_response
        form = ReceipeForm()
        return redirect('/')