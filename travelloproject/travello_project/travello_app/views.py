from django.shortcuts import render
from .models import mydestination,mypeople

# Create your views here.
def demo(request):
    desobj=mydestination.objects.all()
    pobj=mypeople.objects.all()
    return render(request,'index.html',{'desob':desobj,'pob':pobj})
