from django.urls import path,include
from . import views

urlpatterns =[
    path('select/<int:question_id>', views.select,name = "select"),
    # path('create/', views.create,name = "create"),
    path('<int:question_id>/', views.answer,name = "answer"),
]
