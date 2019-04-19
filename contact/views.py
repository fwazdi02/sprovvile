from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm
# Create your views here.


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid:
            messages.success(request, '*** Form submission successful ***')
            form.save()
    return HttpResponseRedirect("{}#contact".format(reverse('index')))

