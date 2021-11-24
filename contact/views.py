from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from .forms import ContactForm
# Create your views here.
def contact (request):
    # print("Tipo peticion: {}",format(request.method))
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            
            # Enviamos el correo y redireccionamos
            subject = "Portafolio Django Nuevo Contacto "
            message = "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content)
            sender = "patricio.leppe@gmail.com"
            recipients = ["patricio.leppe@gmail.com"]
            try:
                send_mail(subject, message, sender, recipients, fail_silently=True)
                # Se envia el correo
                return redirect(reverse("contact")+"?ok")
            except:
                # Ocurrio un error, redireccionamos a Fail
                return redirect(reverse("contact")+"?fail")
    return render(request, "contact/contact.html", {'form':contact_form})