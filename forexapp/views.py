from django.shortcuts import render

# Create your views here.
def HomeView(request):
    return render(request,'index.html')

def FHView(request):
    return render(request,'forexhistorical.html')
