from django.http import HttpResponse,JsonResponse
from main.models import Text,Prefix
import logging
logger = logging.getLogger('django')

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def insert(request):
    result = "test"
    # #word = request.GET.get("word")
    # word = "abc"
    # temp = ""
    # pretemp = None
    # result = "result:\n"
    # for c in word:
    #     pretemp = temp
    #     temp += c
    #     #new_world = Prefix(prefix = word, next_char = [Text(text = "b"),Text(text = "c"),Text(text = "d")])
    #     node = Prefix.objects.filter(prefix = pretemp)
    #     #result += str(node)
    #     result += "node"
    #     result += "\n" 
    return HttpResponse(result)

def qeury(request):
    return JsonResponse({"qeury":request.GET.get("q"), "autocompletions":["a","b","c"]})

