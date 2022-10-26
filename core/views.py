import json

from django.shortcuts import render
from django.http import HttpResponse

from .utils import search

from .forms import ParagraphForm

# Create your views here.


def home_page(request):
    context = {
        'form': ParagraphForm
    }
    return render(request, 'index.html', context)


def check_paragraph(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_paragraph')
        response_data = search(post_text)
    
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )