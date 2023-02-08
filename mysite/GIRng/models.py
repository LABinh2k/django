from django.db import models


class Base(models.Model):

    name = models.CharField(max_length=32, unique=True, blank=False)
    description = models.CharField(max_length=255, blank=True)

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
    level = models.IntegerField(default=90)

    def __str__(self):
        return self.name


class NormalAttack(Base):
    character = models.OneToOneField(Character,
                                     on_delete=models.CASCADE,
                                     primary_key=True,)

    def __str__(self) -> str:
        return self.name


class ElementalSkill(Base):
    cd = models.IntegerField(blank=False)

    character = models.OneToOneField(Character,
                                     on_delete=models.CASCADE,
                                     primary_key=True,)

    def __str__(self) -> str:
        return self.name


class ElementalBurst(Base):
    cd = models.IntegerField(blank=False)

    character = models.OneToOneField(Character,
                                     on_delete=models.CASCADE,
                                     primary_key=True,)

    def __str__(self) -> str:
        return self.name


class Passive(Base):
    character = models.OneToOneField(Character,
                                     on_delete=models.CASCADE,
                                     primary_key=True,)

    def __str__(self) -> str:
        return self.name


class Artifact(Base):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Weapon(Base):
    character = models.OneToOneField(Character,
                                     on_delete=models.CASCADE,
                                     primary_key=True,)

    def __str__(self) -> str:
        return self.name


class Constellation(Base):
    level = models.IntegerField(blank=False)

    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

# luu chi so nhu atk, def, em, ...
# class BaseStat(models.Model):


#     character = models.OneToOneField(Character,
#         on_delete=models.CASCADE,
#         primary_key=True,)

class Team(Base):
    name = models.CharField(max_length=32, unique=True)
    members = models.ManyToManyField(Character, through='TeamInfo')
    resonance = models.CharField(default='N/A', max_length=32)

    def __str__(self):
        return self.name


class TeamInfo(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
