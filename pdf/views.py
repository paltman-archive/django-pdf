from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from pdf.forms import DocumentForm
from pdf.tasks import process_file
from pdf.models import Document


@login_required
def doc_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.user = request.user
            doc.date_uploaded = datetime.utcnow()
            doc.save()
            process_file.delay(doc)
            return HttpResponseRedirect(reverse('pdf_list'))
    else:
        form = DocumentForm()
    return render_to_response('pdf/upload.html', {'form': form}, context_instance=RequestContext(request))


@login_required
def doc_list(request):
    context = {'pdfs': Document.objects.filter(user=request.user)}
    return render_to_response('pdf/list.html', context, context_instance=RequestContext(request))


@login_required
def doc_detail(request, uuid):
    context = {'pdf': Document.objects.get(uuid=uuid)}
    return render_to_response('pdf/detail.html', context, context_instance=RequestContext(request))
