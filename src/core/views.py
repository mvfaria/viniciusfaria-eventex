# coding: utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import TemplateView, DetailView
from django.views.generic.simple import direct_to_template
from .models import Speaker, Talk


class Homepage(TemplateView):
    template_name = 'index.html'

'''
def homepage(request):
    context = RequestContext(request)
    return render_to_response('index.html', context)
'''

class SpeakerDetail(DetailView):
    model = Speaker

'''
def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return direct_to_template(request, 'core/speaker_detail.html', {'speaker': speaker})
'''

'''
class TalksView(TemplateView):
    template_name = 'core/talks.html'

    def get_context_data(self, **kwargs):
        context = super(TalksView, self).get_context_data(**kwargs)
        context.update({
            'morning_talks': Talk.objects.at_morning(),
            'afternoon_talks': Talk.objects.at_afternoon(),
        })
        return context
'''

def talks(request):
    context = {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon(),
    }
    return direct_to_template(request, 'core/talks.html', context)

class TalkDetail(DetailView):
    model = Talk

'''
def talk_detail(request, pk):
    talk = get_object_or_404(Talk, pk=pk)
    context = {
        'talk': talk,
        'slides': talk.media_set.filter(type='SL'),
        'videos': talk.media_set.filter(type='YT'),
    }
    return direct_to_template(request, 'core/talk_detail.html', context)
'''
