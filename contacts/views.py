from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.
def contact(request):
    return render(request, 'pages/contact.html')

def contacted(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contacted = Contact(name=name, email=email, subject=subject, message=message)
        contacted.save()
        messages.success(request, 'Obrigado por entrar em contato, retornaremos em breve!')
        return redirect('/contato/#contact-form-area')

