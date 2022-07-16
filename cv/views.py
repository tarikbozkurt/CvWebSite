from django.shortcuts import render

from cv.models import Informations_me,Educations_me,Job_experience_me,Certifications_me

# Create your views here.
def mainViews(request):
    personelInf = Informations_me.objects.get()


    context = {
        'personelInf':personelInf,
    }
    return render(request,"main/skeleton.html",context)

