from django.shortcuts import render,redirect
from .forms import addQuestionForm, CreateUserForm
from .models import QuesModel
from django.contrib.auth import login,logout,authenticate
# Create your views here.


def home(request):
    if request.method =='POST':
      questions = QuesModel.objects.all()
      score = 0
      wrong = 0
      correct = 0
      total=0
      for q in questions:
        total+=1
        if q.ans == request.POST.get(q.question):
            score += 10
            correct+=1
        else:
           wrong+=1
      percent = score/(total*10)*100
      context={
        'score':score,
        'time':request.POST.get('timer'),
        'correct':correct,
        'wrong':wrong,
        'percent':percent,
        'total':total,
        }
      return render(request,'result.html',context)

    else:
        questions = QuesModel.objects.all()
        context={
            'questions':questions
        }


        return render(request,'home.html',context)


def addQuestion(request):
   
    form = addQuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context={
        'form':form
    }
    return render(request,'addquestion.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'login.html',context)