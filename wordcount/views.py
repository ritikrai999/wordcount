from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	return render(request,'home.html')

def count(request):
	fulltext = request.GET['fulltext']
	wordlist=fulltext.split(" ")
	wordsno=len(wordlist)
	return render(request,'count.html',{'fulltext':fulltext,'wordsno':wordsno})

def aboutus(request):
	return render(request,'aboutus.html')


	

