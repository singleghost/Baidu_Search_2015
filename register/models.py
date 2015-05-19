#coding=utf-8
from django.db import models



class Team(models.Model):
    name = models.CharField(max_length = 30)
    account = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    score = models.IntegerField(default=0,null=True,blank=True)
    time = models.IntegerField(default=0,null=True,blank=True)
    brand = models.IntegerField(default=0,null=True,blank=True)
    def __unicode__(self):
        return u'%s final score is %d ,time used %d' % (self.name,self.score,self.time)

    class Meta:
        ordering = ['score']
class Team_member(models.Model):
    name = models.CharField(max_length = 30)
    sex = models.CharField(max_length = 4)
    phone_number = models.IntegerField()
    phone_number_short = models.IntegerField(default=111111,null=True,blank = True)
    profession = models.CharField(max_length = 30,blank=True)
    student_ID = models.IntegerField()
    team = models.ForeignKey(Team)
    def __unicode__(self):
        return u'%s   号码%d   短号%d     队伍%s' % (self.name, self.phone_number,
                                self.phone_number_short, self.team.name)
