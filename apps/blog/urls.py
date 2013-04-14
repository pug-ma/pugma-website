from django.conf.urls import patterns, url
from django.views.generic import ArchiveIndexView, YearArchiveView
from django.views.generic import MonthArchiveView, DayArchiveView
from django.views.generic import DateDetailView
from django.views.generic import ListView

from .models import Entry

from .views import EntryDetailView


urlpatterns = patterns('',
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        DayArchiveView.as_view(queryset=Entry.objects.valids(), date_field='pub_date', month_format='%m'),
        name='blog_entry_archive_day'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        MonthArchiveView.as_view(
            queryset=Entry.objects.valids(), date_field='pub_date', month_format='%m'),
        name='blog_entry_archive_month'
    ),
    url(r'^(?P<year>\d{4})/$',
        YearArchiveView.as_view(queryset=Entry.objects.valids(), date_field='pub_date'),
        name='blog_entry_archive_year'
    ),
    url(r'^(?P<year>\d+)/(?P<month>[-\w]+)/(?P<day>\d+)/(?P<slug>.*)/$',
        DateDetailView.as_view(queryset=Entry.objects.valids(), month_format='%m', date_field="pub_date"),
        name="blog_archive_date_detail"
    ),
    url(r'^(?P<slug>.*)/$', 
        EntryDetailView.as_view(), 
        name='blog_entry_detail'
    ),
    url(r'^$',
        ArchiveIndexView.as_view(
            queryset=Entry.objects.valids(), date_field='pub_date', paginate_by=10),
        name='blog_entry_list'
    ),
)