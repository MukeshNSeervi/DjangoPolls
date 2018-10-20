from django.shortcuts import get_object_or_404, render
from django.http      import HttpResponse,Http404,HttpResponseRedirect
from django.template  import loader
from .models          import Question,Choice
from django.urls      import reverse
from django.views     import generic
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
         return Question.objects.order_by('-pud_date')[:5]
    #template = loader.get_template('polls/index.html')
    #output = '\t\n'.join([q.question_text for q in latest_question_list])
    #return HttpResponse(template.render(context,request))
    #latest_question_list = Question.objects.order_by('-pud_date')[:5]
    #context = {'latest_question_list': latest_question_list}
    #return render(request,'polls/index.html',context)

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    #question = get_object_or_404(Question,pk=question_id)
    #return render(request,'polls/detail.html',{'question':question})
    #try:
    #    question = models.Question.objects.get(pk=question_id)
    #except models.Question.DoesNotExist:
    #    raise Http404("Question doesn't exist error")
    #return render(request,'polls/detail.html',{'question':question })
    #return HttpResponse("You're loking at question %s ." % question_id)

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    #response = "You are looking at question %s ."
    #question = get_object_or_404(Question,pk=question_id)
    #return render(request ,"polls/results.html",{"question":question})
    #return HttpResponse("You are looking at the result of question %s." % question_id)

def vote(request,question_id):

    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (NameError,keyError,Choice.DoesNotExist):
         return render(request,'polls/details.html',{'question':question,"error_message":"You didn,t make a choice",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
    #return HttpResponse("You are voting on question %s." % question_id)
"""

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        #Return the last five published questions.
        return Question.objects.order_by('-pud_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (NameError,keyError,Choice.DoesNotExist):
         return render(request,'polls/details.html',{'question':question,"error_message":"You didn,t make a choice",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
    #return HttpResponse("You are voting on question %s." % question_id)
"""
