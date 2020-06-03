from django.urls import path,include
from . import views

urlpatterns = [
    path('<int:question_id>', views.question,name="question"),
    path('search/',views.search,name="search"),
    path('new/',views.new,name="new"),
    path('delete/<int:question_id>',views.delete, name="delete"),
    path('edit/<int:question_id>',views.edit, name="edit"),
    path('attend/',views.attend, name = "attend"),
    path('my_question/',views.my_question, name = "my_question"),   # 내 질문 보기  
]