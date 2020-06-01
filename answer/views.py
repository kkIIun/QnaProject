from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Answer
from question.models import Question


def select(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    question = answer.question
    user = answer.user
    user.point += 1
    q_user = question.user
    q_user.point -= 1
    user.save()
    q_user.save()
    
    #  q_user = question.user()
    #  if q_user.point < 10:
    #      q_user.point -= 10
    #      answer.user.point += 10
    #      q_user.save()
    #      answer.user.save()   
    

    answer.selected = False
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
    new_answer.user = request.user
    new_answer.save()
    return redirect('question',request.POST['question_id'])
    # answer -> question 구동 확인되면 바꾸기