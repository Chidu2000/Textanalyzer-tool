from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("hello")
    # params = {"name":"Chidambar","nation":"India"}
    return render(request,'index.html')

def analyze(request):
    djtext = request.GET.get('text','default')
    rempunc = request.GET.get('rempunc','off') 
    fullcaps = request.GET.get('fullcaps','off')
    newlinerem = request.GET.get('newlinerem','off')
    extraspacerem = request.GET.get('extraspacerem','off')
    charcount = request.GET.get('charcount','off')
    print(rempunc)  
    print(djtext)
    
    if rempunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params={'purpose':'Removed puncs','analyzed_text':analyzed}
        
        djtext = analyzed
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
                analyzed = analyzed + char.upper()
        params={'purpose':'Making the characters upper case','analyzed_text':analyzed}
        
        djtext = analyzed 
    if(newlinerem=="on"):
        analyzed=""
        for char in djtext:
            if char !='\n' and char!='\r':
                analyzed = analyzed + char
        params={'purpose':'Making the characters upper case','analyzed_text':analyzed}
        
        djtext = analyzed
    if(extraspacerem=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params={'purpose':'Removing extra spaces','analyzed_text':analyzed}
        
        djtext = analyzed 
    if(charcount=="on"):
        count=0
        for char in djtext:
            if not(char==" "):
                count = count + 1
        params={'purpose':'Counting no. of entered chars','analyzed_text':count}
                           
    if(not(charcount and extraspacerem and newlinerem and rempunc and fullcaps)):
        return HttpResponse("Please select any one of the options and try again") 

    return render(request,'analyze.html',params)       

    