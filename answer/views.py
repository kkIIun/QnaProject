from django.shortcuts import render,get_object_or_404,redirect
from .forms import AnswerForm   # 미디어 변경 부분(form)
from .models import Answer



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

    # new? create?

def new(request):   # 미디어 변경 부분(form)
    if request.method == 'POST':
        form = AnswerForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.pub_date = timezone.now()
            content.save()
            return redirect('question.home',content.id) # 경로 확인 필요
    else:
        form = AnswerForm()
    return render(request,'answer.html',{'form':form}) # 경로 확인 필요

def create(request,answer_id):
    new_answer = Answer()
    new_answer.title = request.POST['title']
    new_answer.body = request.POST['body']
    new_answer.image = request.FILES['image']
    return redirect('answer')
