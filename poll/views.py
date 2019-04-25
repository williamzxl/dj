from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render,get_object_or_404
# Create your views here.
from .models import Question,Choice
from django.http import Http404
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # return Question.objects.order_by('pub_date')[:10]
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'poll/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultView(generic.DetailView):
    model = Question
    template_name = 'poll/results.html'

# def index(request):
#     # return HttpResponse("Hello,world.You are at the poll index")
#     latest_question_list = Question.objects.order_by('pub_date')[:10]
#     # output = ",".join([q.question_text for q in latest_question_list])
#     # template = loader.get_template('poll/index.html')
#     context = {
#         'latest_question_list':latest_question_list,
#     }
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'poll/index.html', context)
#
#
# def detail(request, question_id):
#     # return HttpResponse("Detail:You're looking at question %s." % question_id)
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request, 'poll/detail.html',{'question':question})
#
#
# def results(request, question_id):
#     # response = "Result:You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'poll/results.html', {'question':question})


def vote(request, question_id):
    # return HttpResponse("Vote:You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        print("POST['choice']===>",request.POST['choice'])
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print(selected_choice)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'poll/detail.html',{
            'question':question,
            'error_message':"You did not select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll:results',args=(question.id,)))