from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from .forms import QuestionForm
from .models import Question, Answered

# Create your views here.
def question_index(request):
	return render(request, "question_index.html")

def question_create(request):
	form = QuestionForm(request.POST or None, request.FILES or None)
	#If the request is a POST then the form would be valid
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return HttpResponseRedirect(reverse('index'))
	context = {
		"form":form
	}
	return render(request, "question_create.html", context)
	
def question_present(request, id=None):
	#If no specific id is given get a random row
	queryRow = 0
	if id==None:
		queryRow = Question.objects.random()
		if queryRow == None:
			raise Http404("There are no questions to show")
	else:
		queryRow = get_object_or_404(Question, id=id)
	context = {
		"queryRow":queryRow
	}
	return render(request, "question_present.html",context)



#After a question is submitted we redirect to this view to let the user see the result
def question_submit(request, id, answer):
	#queryRow = Question.objects.get(id=id)
	queryRow = get_object_or_404(Question, id=id)
	if(answer == "yes"):
		queryRow.yesCount = queryRow.yesCount + 1
		queryRow.currentAnswers = queryRow.currentAnswers + 1
		queryRow.save()
	else:
		queryRow.noCount = queryRow.noCount + 1
		queryRow.currentAnswers = queryRow.currentAnswers + 1
		queryRow.save()
	
	#Check if the maximum number of answers have been reached
	if queryRow.currentAnswers >= queryRow.totalAnswers:
		#Add to the answered table
		insertRow = Answered(title=queryRow.title,
							totalAnswers = queryRow.totalAnswers,
							yesCount = queryRow.yesCount,
							noCount = queryRow.noCount)
		insertRow.save()
		queryRow.delete()
	
	context = {
		"answer": answer,
		"queryRow": queryRow,
	}
	return render(request, "question_submit.html", context)


#Create a user account
def new_user(request):
	form = UserForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return HttpResponseRedirect(reverse('index'))
	context = {
		"form":form
	}
	return render(request, "new_user.html", context)

		




	
	
	
		
		

	