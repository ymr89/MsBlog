from django.shortcuts import render
from .forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context



# Create your views here.
def index(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email','')
            contact_message = request.POST.get('contact_message','')

            # Email the profile with the 
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_message': contact_message, })
            content = template.render(context)

            email = EmailMessage("New contact form submission",
                                content,
                                "Your website" +'',
                                ['youremail@gmail.com'],
                                headers = {'Reply-To': contact_email } )
            email.send()
            return render(request, 'contact.html', {'form': form_class,})
            
            
                                 
            
            
    return render(request, 'contact.html', {'form': form_class,})
