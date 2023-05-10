from django.db import models



class Race(models.Model):
    name = models.CharField(max_length=50, unique=True,verbose_name='race',help_text='zadej nazev rasy')

    class Meta:
        verbose_name = 'race'
        verbose_name_plural = 'races'
        ordering = ['name']
    def __str__(self):
        return self.name

class Body_part(models.Model):
    body_part = models.CharField(max_length=50, unique=True,verbose_name='body part',help_text='body part',default='Full body')
    class Meta:
        verbose_name = 'body part'
        verbose_name_plural = 'body parts'
        ordering = ['body_part']

    def __str__(self):
        return self.body_part
# Create your models here.
