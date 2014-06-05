from django.views.generic import TemplateView
from events.models import Event


class DanceView(TemplateView):
    template_name = "dance/dance.html"

    def get_context_data(self, **kwargs):
        context = super(DanceView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        context['show_events'] = Event.objects.filter(type__exact="show")
        return context
