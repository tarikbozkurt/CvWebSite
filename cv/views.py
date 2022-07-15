from django.shortcuts import render

# Create your views here.
def mainViews(request):
    return render(request,"main/skeleton.html",context={})
