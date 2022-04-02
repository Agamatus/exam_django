from django.shortcuts import render
from .models import ContactUsForm
from .models import Portfolio


# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        form = ContactUsForm(name=name, email=email, message=message)
        form.save()
    content = {"portfolio": Portfolio.objects.all()}
    return render(request, 'examsite/index.html', content)
