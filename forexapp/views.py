from django.shortcuts import render
from .models import ForexCurrent,ForexHistoric

# Create your views here.
def HomeView(request):
    return render(request,'index.html')

def FHView(request):
    fh = ForexHistoric.objects.all()
    return render(request,'forexhistorical.html',{'data':fh,'t':"Tet"})

def FCView(request):
    fc = ForexCurrent.objects.all()
    return render(request,'forexcurrent.html',{'data':fc})

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<p class='lead'>It is now %s.</p>" % now
    return html
