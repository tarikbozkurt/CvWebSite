from django.db import models

# Create your models here.
from django.db import models

# Create your models here.



class Courses(models.Model):
    """
    course_name : which courses did u take certificate or member
    """
    course_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.course_name

class Certifications_me(models.Model):
    certifica_name = models.CharField(max_length=150,blank=True)
    certifica_company=models.ForeignKey(Courses,on_delete=models.CASCADE,blank=True)

    certifica_url = models.CharField(max_length=250,blank=True)
    certifica_qualification_id= models.CharField(max_length=250,blank=True)

    certifica_start_date = models.DateField(blank=True)


    certifica_image = models.ImageField(blank=True)




    def __str__(self):
        return self.certifica_name

class Education_Types(models.Model):
    """
    education_type_type : for school degree, exp. Bachelor degree

    """
    education_type = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.education_type
class Educations_me(models.Model):
    """
    name = education school name
    edu_type= foreignKey type of school
    """
    edu_name = models.CharField(max_length=50,blank=True)
    edu_type=models.ForeignKey(Education_Types,on_delete=models.CASCADE,blank=True)
    edu_start_date = models.DateField(blank=True)
    edu_ended_date = models.DateField(blank=True)

    def __str__(self):
        return self.edu_name

class Job_experience_me(models.Model):
    company_name = models.CharField(max_length=100,blank=True)
    job_description = models.TextField(blank=True)
    job_position = models.CharField(max_length=100,blank=True)
    job_start_date = models.DateField(blank=True)
    job_end_date = models.DateField(blank=True)
    still_working = models.BooleanField(blank=True)

    def __str__(self):
        return self.company_name

class Informations_me(models.Model):
    p_name = models.CharField(max_length=50, blank=True)
    p_surname = models.CharField(max_length=50, blank=True)
    p_about = models.TextField(blank=True)
    p_picture = models.ImageField(blank=True)

    p_birth_date = models.DateField(blank=True)


    def __str__(self):
        return self.p_name

