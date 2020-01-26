from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	context_dict = {'boldmessage': 'Crucnchy, creamy, cookie, candy, cupcake!'}
	return render(request, 'rango/index.html', context = context_dict)

def about(request):
	context_dict = {'credits': 'This tutorial has been put together by Karthik.'}
	return render(request, 'about/index.html')