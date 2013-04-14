from django import forms
from django.conf import settings

from tagging.forms import TagField
from redactor.widgets import RedactorEditor

from .models import Entry


class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry

		widgets = {
           'body': RedactorEditor(upload_to='blog/post/'),
        }