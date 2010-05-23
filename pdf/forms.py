import os

from django import forms
from django.utils.translation import ugettext_lazy as _

from pdf.models import Document


class DocumentValidationError(forms.ValidationError):
    def __init__(self):
        msg = _(u'Only PDF files are valid uploads.')
        super(DocumentValidationError, self).__init__(msg)


class DocumentField(forms.FileField):
    """A validating PDF document upload field"""

    def clean(self, data, initial=None):
        f = super(DocumentField, self).clean(data, initial)
        ext = os.path.splitext(f.name)[1][1:].lower()
        if ext == 'pdf' and f.content_type == 'application/pdf':
            return f
        raise DocumentValidationError()


class DocumentForm(forms.ModelForm):
    local_document = DocumentField()

    class Meta:
        model = Document
        fields = ('name', 'local_document')
