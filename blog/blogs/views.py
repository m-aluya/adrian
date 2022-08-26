from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.
def details(request,slug):
    post = get_object_or_404(Post,slug=slug)

    return render(request,'blogs/details.html',{'post':post})
