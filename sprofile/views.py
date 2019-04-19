from django.shortcuts import render
from portfolio.models import Portfolio
from contact.forms import ContactForm
from myprofile.models import Skill

def index(request):
    template_name = 'index.html'
    myskill = Skill.objects.filter(user__id=request.site.myprofile.user.id) 
    myportfolio = Portfolio.objects.publish()
    context = {
        'page_title': 'Home',
        'contact_form': ContactForm,
        'myskill': myskill,
        'myportfolio': myportfolio,
    }
    return render(request, template_name, context)

