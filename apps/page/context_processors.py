from apps.projects.models import Project
from apps.blog.models import Entry

def projects(request):
    return {'projects': Project.objects.all()}

def next_event(request):
    event = Entry.objects.filter(is_event=True).order_by('-pub_date')
    try:
        event = event[0]
    except IndexError:
        event = None
    return {'next_event': event}
