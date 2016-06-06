from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
import random

def get_user_default_id():
    return 1

# Create your models here

class QuestionManager(models.Manager):
	#Gets a random row from the table
	def random(self, user=None):
		if user == None or user.is_authenticated():
			count = Question.objects.all().count()
			if count == 0:
				return None
			else:
				random_index = random.randint(0, count - 1)
				return self.all()[random_index]
		else:
			count = Question.objects.exclude(user=user).count()
			if count == 0:
				return None
			else:
				random_index = random.randint(0, count - 1)
				return self.exclude(user=user)[random_index]


	
class Question(models.Model):
	title = models.CharField(max_length=144)
	totalAnswers = models.IntegerField()
	currentAnswers = models.IntegerField(default=0)
	yesCount = models.IntegerField(default=0)
	noCount = models.IntegerField(default=0)
	objects = QuestionManager()
	user = models.ForeignKey(settings.AUTH_USER_MODEL,default=get_user_default_id)
	
	def __unicode__(self):
		return self.title


	
#After a question has received all of it's answers, it will be removed from
#The Question table and placed into the answered table

class Answered(models.Model):
	title = models.CharField(max_length=144)
	totalAnswers = models.IntegerField()
	yesCount = models.IntegerField()
	noCount = models.IntegerField()
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=get_user_default_id)
	
	def __unicode__(self):
		return self.title

	