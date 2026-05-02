from time import timezone

from django.contrib import messages

from django.shortcuts import render
from application.models import Announcement, Festival, enquiryform


# Create your views here.
def home(request):
    announcements = Announcement.objects.filter(
        is_active=True,
       #expiry_date__gte=timezone.now().date()  # only non-expired 
    )
    return render(request,'index.html', {
        'announcements': announcements})

def about(request):
    festivals = Festival.objects.all()
    return render(request, 'about.html', {
        'festivals': festivals
    })

    

def agriculture(request):
    return render(request,'agriculture.html')

def infrastructure(request):
    return render(request,'infrastructure.html')

def economy(request):
    return render(request,'economy.html')

def contact(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('phone')
        c = request.POST.get('subject')
        d = request.POST.get('message')
        enquiry = enquiryform(name = a, phone = b, subject = c, message = d)
        enquiry.save()

        messages.success(request, 'Enquiry Form Submitted Successfully...')
    return render(request,'contact.html')

def education(request):
    return render(request,'education.html')

def millbazaar(request):
    return render(request,'millbazaar.html')

def adminpage(request):
    return render(request,'dashboard/index.html')

