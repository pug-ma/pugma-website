from apps.projects.models import Project
from apps.blog.models import Entry


def latest_entries(request):
    return {'latest_entries': Entry.objects.valids()[:4]}


def projects(request):
    return {'projects': Project.objects.all()}
