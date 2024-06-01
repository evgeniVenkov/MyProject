from django.shortcuts import render


def home(request):
    numslov = [{'one':1,
            'two':2,
            'three':3
            },
             {'one': 4,
             'two': 5,
             'three': 6
             }]
    data = {'number':numslov,
            'title':"titlevalue"}
    return render(request, 'blog/home.html',data)
def about(request):
    return render(request, 'blog/about.html')