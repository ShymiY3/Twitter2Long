from django.shortcuts import render
from .text_split import split_text

def index(request):
    user_text = ''
    parts = []
    if request.method == 'POST':
        user_text = request.POST.get("user_text")
        parts = split_text(user_text)

    context ={
        'user_text':user_text,
        'parts':parts
    }
    return render(request, 'Twitter2LongApp/index.html', context)

