from django import forms
from django.conf import settings

#from tagging.fields import TagField
from tagging.forms import TagField
from redactor.widgets import RedactorEditor

from .models import Entry


class EntryForm(forms.ModelForm):
	tags = TagField()

	class Meta:
		model = Entry

		widgets = {
           'body': RedactorEditor(upload_to='blog/post/'),
        }