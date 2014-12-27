from django.http import HttpResponse
from designweb import tests

# Create your views here.
def index(request):
    msg = tests.db_read()
    # return HttpResponse("Hello, this is hook-up design website...")
    return HttpResponse(msg)
