from django.db import models
from django.utils import timezone
import datetime
# Models are used to create an Database and Following Class Names as their Table names!! @^_^@
# Create your models here.
class Question(models.Model):
    """
        This will create an DB table named Question with the following variables as attribute
    """
    question_text = models.CharField(max_length=200)
    pud_date = models.DateTimeField('Date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pud_date >=timezone.now()
    datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    def __str__ (self):
        return self.choice_text
