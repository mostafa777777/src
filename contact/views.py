
# Create your views here.
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  # يمكنك إنشاء صفحة نجاح
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})