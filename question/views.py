from django.shortcuts import render,get_object_or_404,redirect
from .forms import QuestionForm
from .models import Question
from django.utils import timezone
from answer.models import Answer
from account.models import CustomUserModel

def home(request):
    questions = Question.objects.all()
    return render(request,'home.html',{'questions': questions})

def question(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    answers = Answer.objects.filter(question_id = question.id)
    return render(request,'question.html',{'question':question, 'answers': answers})

def search(request):
    q = request.GET.get('q')

    questions = Question.objects.filter(
            title__icontains=q
        ) | Question.objects.filter(
            body__icontains=q
        ) | Question.objects.filter(
            professor_name__icontains=q
        )
    """
    answers = Answer.objects.filter(
            title__icontains=q
        ) | Answer.objects.filter(
            body__icontains=q
    )
    """

    return render(request,'search.html',{'questions':questions})
    

def new(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid :
            content = form.save(commit=False)
            content.pub_date = timezone.now()
            content.user = request.user
            content.save()
            return redirect('question',content.id)
    else :
        form = QuestionForm()
        return render(request,'new.html',{'form':form})

def edit(request,question_id):
    question = get_object_or_404(Question,pk=question_id)

    if request.method == 'POST':
        form = QuestionForm(request.POST,instance= question)
        if form.is_valid :
            question = form.save()
            return redirect('question',question.id)

    else :
        form = QuestionForm(instance=question)
        return render(request,'edit.html',{'form':form})

def delete(request,question_id):
    delete_question = get_object_or_404(Question, pk = question_id)
    delete_question.delete()
    return redirect('home')


# Create your views here.

