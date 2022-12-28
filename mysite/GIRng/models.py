import random

from django.db import models

# Create your models here.    
class Character(models.Model):
    name = models.CharField(max_length=32)
    ELEMENT_CHOICES = [
        ('Pyro', 'Pyro'),
        ('Cryo', 'Cryo'),
        ('Hydro', 'Hydro'),
        ('Geo', 'Geo'),
        ('Anemo', 'Anemo'),
        ('Electro', 'Electro'),
        ('Dendro', 'Dendro')
    ]
    
    element = models.CharField(max_length=7, choices=ELEMENT_CHOICES)
    
    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=32)
    members = models.ManyToManyField(Character, through='TeamInfo')
    
    def __str__(self):
        return self.name
        
        
class TeamInfo(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
    resonance = models.CharField(max_length=32)
    description = models.TextField()

    