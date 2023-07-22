from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Subscriber, Newsletter
from django.contrib import messages


# Create your views here.

def index(request):
   
   if request.method == "POST":                    
        email = request.POST.get('email')

        if Subscriber.objects.filter(email=email).exists():
            messages.success(request, f'You already subscribed with us!')
            return redirect( 'index') 

        subscriber = Subscriber(email=email)
        subscriber.save() 
        messages.success(request, f'Thank you subscribing to our NewsLetter!')
        return render(request, 'index.html')   
                       
   else:
      return render(request, 'index.html')



def about(request):

    return render(request, 'about.html') 



        


