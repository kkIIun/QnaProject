from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
import pdb
from .models import Answer
from question.models import Question


def select(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    question = answer.question
    
    # q_user = question.user
    # if q_user.point < 10:
    #     q_user.point -= 10
    #     answer.user.point += 10
    #     q_user.save()
    #     answer.user.save()   
    

    answer.selected = True
    answer.save()
    
    return redirect('question', question.id)


def answer(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    return render(request,'answer.html',{'question':question})

def create(request):
    new_answer = Answer()
    new_answer.title = request.POST['title']
    new_answer.body = request.POST['body']
    new_answer.pub_date = timezone.now()
    new_answer.selected = 1
    new_answer.question = get_object_or_404(Question, pk=request.POST['question_id'])
    new_answer.save()
    return redirect('question',request.POST['question_id'])
    # answer -> question 구동 확인되면 바꾸기