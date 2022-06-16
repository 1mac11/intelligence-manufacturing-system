from django.conf import settings
from django.db import models
from core.models import BaseModel


class LevelChoice(models.TextChoices):
    TRAINEE = ('trainee', 'Trainee')
    JUNIOR = ('junior', 'Junior')
    MIDDLE = ('middle', 'Middle')
    SENIOR = ('senior', 'Senior')
    TEAM_LEAD = ('team_lead', 'Team Lead')
    TECH_LEAD = ('tech_lead', 'Tech Lead')
    HEAD = ('head', 'Head of Department')


class UserDetail(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='detail')
    birth_date = models.DateTimeField(blank=True, null=True)
    salary = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    level = models.CharField(choices=LevelChoice.choices, max_length=100)
    type = models.ForeignKey('core.UserType', on_delete=models.SET_NULL, related_name='users', null=True, blank=True)

    class Meta:
        verbose_name = 'user detail'
        verbose_name_plural = 'user details'

    def __str__(self):
        return self.user.__str__()
