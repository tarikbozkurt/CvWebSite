from django.db import models

# Create your models here.

class cvMenus(models.Model):
    m_menu_name = models.CharField(max_length=50,blank=True)
    m_menu_ıcon = models.ImageField(blank=True)

    def __str__(self):
        return self.m_menu_name