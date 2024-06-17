# i have created this file
from django.http import HttpResponse
from django.shortcuts import render
import string
def index(request):
   return render(request,"index.html")
def removepuce(request):
    djtext=request.POST.get('text','default')
    removepuc=request.POST.get('removepuce','off')
    uppercase=request.POST.get('capitlize','off')
    newlineremove=request.POST.get('newlineremove','off')
    removeextraspace=request.POST.get('removeextraspace','off')
    charcount=request.POST.get('charcount','off')
    if removepuc=='on':
        anali=""
        punchuation=string.punctuation
        for i in djtext:
            if i not in punchuation:
                anali=anali+i
        djtext=anali
    if(uppercase=='on'):
        captlize=""
        for i in djtext:
            captlize=captlize+i.upper()
        djtext=captlize
    if(newlineremove=="on"):
        newline=''
        for i in djtext:
            if i!='\n' and i!='\r':
                newline=newline+i
        # newline=''.join(djtext.splitlines()) #hum direct ishka bhi use kar sakte hai
        print(newline)
        djtext=newline
    if(removeextraspace=="on"):
        exraspce=""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                exraspce=exraspce+char
        djtext=exraspce
       
    if(charcount=="on"):
        count=0
        coun=''.join(djtext.splitlines())
        for i in coun:
            if i==" ":
                pass
            else:
             count=count+1
        rp={'purpose':'total charactor','analyze_text':djtext,'countchar':count}
        return render(request,'analize.html',rp)
    elif (removepuc=='on') or (uppercase=='on') or (newlineremove=='on') or (removeextraspace=='on'):
         rp={'purpose':'done','analyze_text':djtext}
         return render(request,'analize.html',rp)

    else:
        return HttpResponse("error")