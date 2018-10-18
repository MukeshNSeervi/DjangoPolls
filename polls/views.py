from django.shortcuts import get_object_or_404, render
from django.http      import HttpResponse,Http404
from django.template  import loader
from .                import models
# Create your views here.

def princess(request):
    latest_question_list = models.Question.objects.order_by('-pud_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    #output = '\t\n'.join([q.question_text for q in latest_question_list])
    #return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    question = get_object_or_404(models.Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})
    #try:
    #    question = models.Question.objects.get(pk=question_id)
    #except models.Question.DoesNotExist:
    #    raise Http404("Question doesn't exist error")
    #return render(request,'polls/detail.html',{'question':question })
    #return HttpResponse("You're loking at question %s ." % question_id)

def results(request,question_id):
    #response = "You are looking at question %s ."
    return HttpResponse("You are looking at the result of question %s." % question_id)

def vote(request,question_id):
    return HttpResponse("You are voting on question %s." % question_id)
