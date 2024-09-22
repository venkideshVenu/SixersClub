
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def get_home_page(request):
    return render(request, 'home/homepage.html',context={})

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            # Debugging output
            print(f"Subject: {subject}, Message: {message}, From: {email}, To: {settings.DEFAULT_FROM_EMAIL}")

            send_mail(subject, message, email, [settings.DEFAULT_FROM_EMAIL])
            return render(request, 'home/contact.html', {'form': form, 'success': True})
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})
