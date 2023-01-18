import random

from django.db import models

class Base(models.Model):

    name = models.CharField(max_length=32, unique= True)
    # description = models.CharField(max_length=255)
    class Meta:
        abstract = True    

class Character(Base):
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
    # level = models.IntegerField()
    # action: danh sach cac hanh dong mot character co the lam
    # actions = models.OneToManyField(Action)
    # passives = models.OneToManyField(Passive)
    # artifacts = models.OneToManyField(Artifact)
    # weapon = models.OneToOneField(Weapon)
    # basestat = models.OneToOneField(BaseStat)
    # constellations = models.OneToManyField(Constellation)

    def __str__(self):
        return self.name
# class NormalAttack(Base):
#     pass

# class ElementalSkill(Base):
#     pass

# class ElementalBurst(Base):
#     pass

# class Passive(Base):
#     pass

# class Artifact(Base):
#     pass

# class Weapon(Base):
#     pass

# class Constellation(Base):
#     pass

# class BaseStat(models.Model):
#     pass    

class Team(Base):
    name = models.CharField(max_length=32, unique=True)
    members = models.ManyToManyField(Character, through='TeamInfo')
    
    def __str__(self):
        return self.name
        
        
class TeamInfo(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
    resonance = models.CharField(max_length=32)
    description = models.TextField()

    