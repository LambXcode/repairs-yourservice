from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        company = request.POST.get('company')
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        os = request.POST.get('os')
        category = request.POST.get('category')
        description = request.POST.get('description')

        print(f'Name: {name}\nEmail: {email}\nCompany: {company}\nBrand: {brand}\nModel: {model}\nOS: {os}\nCategory: {category}\nDescription: {description}')

        subject = 'Thank you for contacting us'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['mlamb.info@gmail.com','michaellamblife@gmail.com']

        html_message = render_to_string(
            'repairs/email_body.html',
            {
                'name': name,
                'email': email,
                'company': company,
                'brand': brand,
                'model': model,
                'os': os,
                'category': category,
                'description': description
            }
        )

        plain_message = strip_tags(html_message)

        send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)

        return render(request, 'repairs/confirmation_form.html')

    return render(request, 'repairs/contact_form.html')
