from django.urls import path,include
from . import views

urlpatterns =[
    path('select/<int:answer_id>', views.select,name = "select"),
    path('<int:question_id>/', views.answer,name = "answer"),
    path('a_delete/<int:answer_id>',views.delete, name="a_delete"),
    path('a_edit/<int:answer_id>',views.edit, name="a_edit"),
]
