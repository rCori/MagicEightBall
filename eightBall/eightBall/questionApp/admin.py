from django.contrib import admin

# Register your models here.

from .models import Question, Answered

class QuestionAdmin(admin.ModelAdmin):
	list_display =['title', 'totalAnswers', 'currentAnswers', 'yesCount', 'noCount']
	
class AnsweredAdmin(admin.ModelAdmin):
	list_display =['title', 'totalAnswers', 'yesCount', 'noCount']
	
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answered, AnsweredAdmin)
