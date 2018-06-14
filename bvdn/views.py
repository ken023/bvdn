from django.shortcuts import render
import json
from users.models import User
from tool_03.models import Blog

def index(request):
    a = Blog.objects.all().order_by('-id')[:5]
    return render(request, 'baseMain.html', {'blogs':a})

def profile(request):
    if request.method == 'POST':
        a = json.loads(request.body)
        print(a)
        b = User.objects.get(email=request.user.email)
        b.name = a['name']
        b.save()
    return render(request, 'account_profile.html')