from django.http import HttpResponse,JsonResponse
from main.models import Prefix
import logging
logger = logging.getLogger('django')

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def insert(request):
    result = "test"
    word = request.GET.get("word")
    word = list(word)
    word.append("")
    temp = ""
    pretemp = None
    result = "result:\n"
    for c in word:
        pretemp = temp
        temp += c
        querySet = Prefix.objects(prefix = pretemp)
        if len(querySet) == 0 :
            new_word = Prefix(prefix = pretemp, next_char = [])
        elif len(querySet) == 1 :
            new_word = querySet[0]
        else :
            raise Exception("NOT IMPLEMENT")
        if c not in new_word.next_char:
            new_word.next_char.append(c)
        new_word.save()
    return HttpResponse("inserted!")

def query(request):
    #return JsonResponse({"qeury":request.GET.get("q"), "autocompletions":["a","b","c"]})
    q = request.GET.get("q")
    autocompletion = collectContainedWords(q)
    return JsonResponse({"autocompletion":autocompletion})

def collectContainedWords(prefix):
    #prefix不存在 return empty list
    querySet = Prefix.objects(prefix = prefix)
    if len(querySet) == 0:
        return []
    if len(querySet) > 1:
        raise Exception("NOT IMPLEMENT")
    #step1:找到本node下面的直属的完整的词
    autocompletion = []
    document = querySet[0]
    if "" in document.next_char:
        autocompletion.append(document.prefix)
    #找到所有的children node
    for c in document.next_char:
        if c == "":
            continue
        #把每个child node下属的词都放入return里面
        childprefix = prefix + c
        autocompletion.extend(collectContainedWords(childprefix)) 
    return autocompletion

