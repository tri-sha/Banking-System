from django.shortcuts import render,redirect
from .models import Customer,Transfer
from django.contrib import messages
from datetime import datetime
def home(request):
    return render(request,"griphome.html")

def showcustomer(request):
    customers=Customer.objects.all()
    return render(request,'customertab.html',{'customers':customers})

def profile(request):
    cobj=Customer.objects.get(id=int(request.GET['id']))
    return render(request,'customerprofile.html',{'cobj':cobj})  
    
def transfermoney(request): 
    if request.method=='GET':
        sender_id=int(request.GET['id'])
        return render(request,'transferform.html',{'sender_id':sender_id})
    else:
        sendmoney=int(request.POST['amount'])
        sender=Customer.objects.get(id=int(request.POST['sender_id']))
        receiver=Customer.objects.get(name=str(request.POST['name']))
        if sender.currentbal < sendmoney:
            messages.info(request,"Not Sufficient balance")
            return render(request,'customerprofile.html',{'cobj':sender})
        elif not receiver: 
            messages.info(request,"Incorrect Customer Name")
            return render(request,'customerprofile.html',{'cobj':sender})
        
        elif sender.name == receiver.name :
            messages.info(request,"Same name not possible")
            return render(request,'customerprofile.html',{'cobj':sender})   
        
        else:    
            sender.currentbal=sender.currentbal - (sendmoney)
            receiver.currentbal=receiver.currentbal+(sendmoney)
            sender.save()
            receiver.save()
            now = datetime.now()
            tobj=Transfer(sender=sender.name,receiver=receiver.name,amount=sendmoney,transfertime=now)
            tobj.save()
            print("Successful")
            return redirect('/showcustomer')  


def transferhistory(request):
    tobj=Transfer.objects.all()
    return render(request,'transferhistory.html',{'tobj':tobj})

        