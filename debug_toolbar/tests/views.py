
from django.shortcuts import render_to_response

def test_view(request, formClass):
    return render_to_response('debug_toolbar/redirect.html')
