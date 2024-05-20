from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def calculate(request):
    if(request.method=='POST'):
        val1=int(request.POST['num1'])
        val2=int(request.POST['num2'])
        oper=request.POST['operation']
        if(oper=='add'):
            result=val1+val2
        elif(oper=='subtract'):
            result=val1-val2
        elif(oper=='multiply'):
            result=val1*val2
        elif(oper=='divide'):
            if(val2!=0):
                result=val1/val2
            else:
                return HttpResponse("Cannot divide by Zero")
        else:
            return HttpResponse("Invalid Operation")
        context={
            "result":result
        }
        return render(request, 'result.html',context)



            
