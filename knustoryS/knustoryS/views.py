from django.shortcuts import (
    render_to_response, render
)
from django.template import RequestContext

def index(request):
    return render(request, 'index.html')

# HTTP Error 400
def bad_request(request):
    response = render_to_response(
        '400.html',
        context_instance=RequestContext(request)
    )
    response.status_code = 400
    return response
