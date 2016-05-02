from django.test import TestCase
from .models import Question
from django.core.urlresolvers import reverse

# Create your tests here.
class QuestionModelTests(TestCase):

	def test_starts_with_no_answers(self):
		new_question = Question(title="test question", totalAnswers=5)
		self.assertEqual(new_question.currentAnswers,0)
		
	def test_random_with_no_entry_returns_null(self):
		new_question = Question.objects.random()
		self.assertEqual(new_question,None)
		
class ViewResponseTests(TestCase):
	
	def test_response_index(self):
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)
		
	def test_response_create(self):
		response = self.client.get(reverse('create'))
		self.assertEqual(response.status_code, 200)
		
	def test_response_present_no_id_no_entry(self):
		response = self.client.get(reverse('present'))
		self.assertEqual(response.status_code, 404)
	
	def test_response_present_no_id_one_entry(self):
		new_question = Question(title="test question", totalAnswers=5)
		new_question.save()
		response = self.client.get(reverse('present'))
		self.assertEqual(response.status_code, 200)
		
	def test_response_present_with_id(self):
		new_question = Question(title="test question", totalAnswers=5)
		new_question.save()
		response = self.client.get(reverse('present', args=[new_question.id]))
		self.assertEqual(response.status_code, 200)
		
	def test_response_present_with_id_get_404(self):
		new_question = Question(title="test question", totalAnswers=5)
		new_question.save()
		response = self.client.get(reverse('present', args=[5]))
		self.assertEqual(response.status_code, 404)