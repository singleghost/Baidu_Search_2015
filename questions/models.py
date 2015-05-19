from django.db import models

class Questions(models.Model):
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=50)
    def __unicode__(self):
        return self.answer

