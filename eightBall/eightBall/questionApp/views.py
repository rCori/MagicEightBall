from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from .forms import *
from .models import Question, Answered
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def question_index(request):
	return render(request, "question_index.html")

@login_required(login_url='/questionApp/accounts/login/')
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
		queryRow = Question.objects.random(request.user)
		if queryRow == None:
			 return HttpResponse("<p>There are no questions you can answer</p>")
	else:
		queryRow = get_object_or_404(Question, id=id)
	context = {
		"queryRow":queryRow
	}
	return render(request, "question_present.html",context)



#After a question is submitted we redirect to this view to let the user see the result
def question_submit(request, id, answer):
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
							noCount = queryRow.noCount,
							user = queryRow.user)
		insertRow.save()
		queryRow.delete()
	
	context = {
		"answer": answer,
		"queryRow": queryRow,
	}
	return render(request, "question_submit.html", context)

@login_required(login_url='/questionApp/accounts/login/')
def user_profile(request):
	#If no specific id is given get a random row
		
	user_questions = None
	try:
		user_questions = Question.objects.filter(user=request.user).values()
	except Question.DoesNotExist:
		user_questions = None
	
	user_answers = None
	try:
		user_answers = Answered.objects.filter(user=request.user).values()
	except Answered.DoesNotExist:
		user_answers = None
	
	context = {
		"user_questions": user_questions,
		"user_answers": user_answers,
	}
	return render(request,"user_profile.html", context)
	
	
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def login_page(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
		else:
			form = LoginForm()
			variables = RequestContext(request, {'form': form, 'error':True})
			return render(request,'registration/login.html',variables)
	else:
		form = LoginForm()
		variables = RequestContext(request, {'form': form, 'error':False})
		return render(request,'registration/login.html',variables)
	
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect(reverse('register_success'))
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )