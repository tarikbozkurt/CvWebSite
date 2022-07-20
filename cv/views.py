from django.shortcuts import render

from cv.models import Informations_me,Educations_me,Job_experience_me,Certifications_me,Abilities,Sub_Abilities,SocialMedia
from rootCv.models import cvMenus
# Create your views here.
def mainViews(request):
    personelInf = Informations_me.objects.get()
    my_educations = Educations_me.objects.all()
    my_Job_Experiences = Job_experience_me.objects.all()
    my_Certifications = Certifications_me.objects.all()
    my_cvMenu = cvMenus.objects.all()
    my_Abilities = Abilities.objects.all()
    my_SubAbilities = Sub_Abilities.objects.all()
    my_social_medias = SocialMedia.objects.all()
    context = {
        'personelInf':personelInf,
        'my_educations':my_educations,
        'my_Job_Experiences':my_Job_Experiences,
        'my_Certifications':my_Certifications,
        'my_CvMenu':my_cvMenu,
        'my_Abilities':my_Abilities,
        'my_SubAbilities':my_SubAbilities,
        'my_social_medias':my_social_medias,
    }
    return render(request,"main/skeleton.html",context)

