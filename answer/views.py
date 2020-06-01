from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .forms import AnswerForm
from .forms import Answer
from question.models import Question    # 이거 맞나?


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


def answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST, request.FILES)
        if form.is_valid :
            content = form.save(commit=False)
            content.pub_date = timezone.now()
            content.user = request.user
            content.save()
            return redirect('answer',content.id)
    else :
        form = AnswerForm()
        return render(request,'answer.html',{'form':form})  # {'question':question}

# def create(request):
#     new_answer = Answer()
#     new_answer.title = request.POST['title']
#     new_answer.body = request.POST['body']
#     new_answer.pub_date = timezone.now()
#     new_answer.selected = 1
#     new_answer.question = get_object_or_404(Question, pk=request.POST['question_id'])
#     new_answer.save()
#     return redirect('question',request.POST['question_id'])
#     # answer -> question 구동 확인되면 바꾸기

    # title = models.CharField(max_length=200)
    # pub_date = models.DateTimeField()
    # body = models.TextField()
    # image = models.ImageField(upload_to="answer/", blank=True, null=True) # 이미지 받는 필드  # media/answer/파일이름 -> 이렇게 저장 된다
    
    # selected = models.BooleanField(null=False, default=False)

    # question = models.ForeignKey(Question, on_delete=models.CASCADE)

    