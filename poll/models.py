from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=300)
    factor = models.CharField(max_length=2, default='null')
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    key = models.CharField(max_length=1)
    point = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text