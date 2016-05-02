from django.db import models
from django.core.urlresolvers import reverse
import random

# Create your models here.

class QuestionManager(models.Manager):
	#Gets a random row from the table
	def random(self):
		count = Question.objects.all().count()
		if count == 0:
			return None
		else:
			random_index = random.randint(0, count - 1)
			return self.all()[random_index]
		
		
class Question(models.Model):
	title = models.CharField(max_length=144)
	totalAnswers = models.IntegerField()
	currentAnswers = models.IntegerField(default=0)
	yesCount = models.IntegerField(default=0)
	noCount = models.IntegerField(default=0)
	objects = QuestionManager()
	
	def __unicode__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"slug": self.slug})


	
#After a question has received all of it's answers, it will be removed from
#The Question table and placed into the answered table

class Answered(models.Model):
	title = models.CharField(max_length=144)
	totalAnswers = models.IntegerField()
	yesCount = models.IntegerField()
	noCount = models.IntegerField()
	
	def __unicode__(self):
		return self.title

	