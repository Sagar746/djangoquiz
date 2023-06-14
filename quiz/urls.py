from django.urls import path
from .views import loginPage,home, addQuestion

urlpatterns = [
    path('', home, name='home'),
    path('addquestion/', addQuestion,name='addquestion'),
    path('login/', loginPage,name='login'),
]