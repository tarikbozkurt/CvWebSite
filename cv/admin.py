from django.contrib import admin

# Register your models here.
from cv.models import *
# Register your models here.
admin.site.register(Courses)

admin.site.register(Educations_me)

admin.site.register(Education_Types)

admin.site.register(Certifications_me)

admin.site.register(Job_experience_me)

admin.site.register(Informations_me)

admin.site.register(Abilities)

admin.site.register(Sub_Abilities)


admin.site.register(SocialMedia)