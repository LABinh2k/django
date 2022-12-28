import datetime
from typing import Any
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.pub_date = timezone.now()
        super().__init__(*args, **kwargs)
        
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now =  timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)    
        
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
        
    def __str__(self):
        return self.choice_text