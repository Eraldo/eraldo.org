from django.db.models import Q
from django.views.generic import TemplateView
from dance.models import Instructor, Group
from events.models import Event


class DanceView(TemplateView):
    template_name = "dance/dance.html"

    def get_context_data(self, **kwargs):
        context = super(DanceView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        context['show_events'] = Event.objects.filter(type__exact="show")
        context['instructors'] = Instructor.objects.filter(Q(gender__exact='M') | Q(partner__isnull=True)).distinct()
        context['personal_trainer'] = Instructor.objects.get(type__exact="coach")
        context['groups'] = Group.objects.all()
        return context
