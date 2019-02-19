from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

@csrf_exempt
def look_log(request):
    a = {'a':''}
    return render(request, 'tools/look_log.html', a)

@csrf_exempt
def get_log(request):
    str_ = []
    fname = 'logs/tools.log'
    with open(fname, 'r') as f:  # 打开文件
        lines = f.readlines()
        count = len(lines)
        if count > 100:
            num = 100
        else:
            num = count
        i = 1
        for i in range(1, (num + 1)):
            if lines:
                n = -i
                last_line = lines[n].strip()
                # print "last line : ", last_line
                f.close()
                # print i
                str_.append(last_line)

    return JsonResponse(str_, safe=False)