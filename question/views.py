from django.shortcuts import render,get_object_or_404,redirect
from .forms import QuestionForm
from .models import Question
from django.utils import timezone
from answer.models import Answer
from account.models import CustomUserModel
from django.utils.timezone import localdate
from django.core.paginator import Paginator

def home(request):
    question = Question.objects
    q_list = Question.objects.all()
    paginator = Paginator(q_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'home.html',{'question': question, 'posts' : posts})

# 페이지네이션 코드 시작
    # qeustion = Question.objects
    # paginator = Paginator(home_card, 3)  # 첫 번째는 분할 될 객체, 두 번째는 한 페이지에 담길 객체의 개수
    # page = request.GET.get('page')
    # posts = paginator.get_page(page)    # page번호 받아서 해당 page 리턴해준다
    # return render(request, 'home.html', {'question':question,'posts',posts}) # render함수로 posts를 넘겨준다
# 페이지네이션 코드 끝( 기존 return은 지워야 함! )


# 아래는 home.html에 기존 카드에 대신해 넣을 페이지네이션 코드, html에서 주석처리가 안되길래 여기다 넣어둠
# 문제가 뭘까
    # <div class="container">
    #     <h3>답변을 기다리는 질문</h3>
    #     <hr>
    #     {% if posts %}
    #     {% for question in posts %}
    #     <div class="card p-3 my-3" name="home_card">
    #         <a href="{%url 'question' question.id%}" id="content">
    #             <h3>{{question.title}}</h3>
    #             교수명:{{question.professor_name}} 교수님
    #             과목명:{{question.subject_name}}
    #             <p style="text-align: right; margin: -1.3rem; padding-right:1rem;padding-bottom:0.7rem;color:grey;">{{question.pub_date}}</p>
    #         </a>
    #     </div>
    #     {% endfor %}
    # </div>

    #         {% if posts.has_previous %}
    #         <a href="?page={{posts.previous_page_number}}"> « </a>
    #         {% endif %}
    #         <span>{{ posts.number }}</span>
    #         <span>/</span>
    #         <span>{{ posts.paginator.num_pages }}</span>
    #         {% if posts.has_next %}
    #         <a href="?page={{posts.previous_page_number}}"> » </a>
    #         {% endif %}
    #     {% endif %}
    # {% endblock %}

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

def attend(req):
    print(localdate())
    if localdate() != req.user.last_signed_at : 
        req.user.last_signed_at = localdate()
        req.user.point += 5
        req.user.save()
        return redirect('home')

    else :
        return redirect('home')



# Create your views here.

