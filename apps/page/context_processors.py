from datetime import datetime
from apps.projects.models import Project
from apps.blog.models import Entry
from apps.schedule.models import Event


def latest_entries(request):
    return {'latest_entries': Entry.objects.valids()[:4]}

def projects(request):
    return {'projects': Project.objects.all()}

def schedule(request):
    events = Event.objects.filter(date__gte=datetime.now).order_by('-date')
    return {'schedule': events}
