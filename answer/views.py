from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .forms import AnswerForm
from .forms import Answer
from question.models import Question   


def select(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    question = answer.question
    user = answer.user
    if q_user.point > 10:
        user.point += 1
        q_user = question.user
        q_user.point -= 1
        user.save()
        q_user.save()

    #  q_user = answer.question.user()
    #  if q_user.point < 10:
    #      q_user.point -= 10
    #      answer.user.point += 10
    #      q_user.save()
    #      answer.user.save()

    answer.selected = True
    print(answer.selected)
    answer.save()
    return redirect('question', question.id)


def answer(request,question_id):
    if request.method == 'POST':
        form = AnswerForm(request.POST, request.FILES)
        if form.is_valid :
            content = form.save(commit=False)
            content.pub_date = timezone.now()
            content.user = request.user
            content.question = get_object_or_404(Question, pk=question_id)
            content.save()
            return redirect('question',question_id)

    else :
        form = AnswerForm()
        return render(request,'answer.html',{'form':form}) 

def edit(request,answer_id):
    answer = get_object_or_404(Answer,pk=answer_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST,instance= answer)
        if form.is_valid :
            answer = form.save()
            return redirect('question',answer.question.id)

    else :
        form = AnswerForm(instance=answer)
        return render(request,'edit.html',{'form':form})

def delete(request,answer_id):
    delete_answer = get_object_or_404(Answer, pk = answer_id)
    delete_answer.delete()
    return redirect('question',delete_answer.question.id)
