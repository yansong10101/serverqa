from django.http import HttpResponse
from designweb import tests
from designweb.models import test_db

# Create your views here.
def index(request):
    # msg = tests.db_read()
    msg = test_db.cust_objects.get_all().count()
    # return HttpResponse("Hello, this is hook-up design website...")
    return HttpResponse(msg)
