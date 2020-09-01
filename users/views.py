from django.shortcuts import render
from django.core.mail import send_mail

send_mail(
    subject = 'ACCOUNT ACTIVATION'
    message = 'Click the below link to activate your account'
    from_email = 'projectsdata33@gmail.com'
    recipient_list = ['email',]
    auth_user = 'Login'
    auth_password = 'Password'
    fail_silently = True,
)


from django.shortcuts import render
from customuser.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
# Create your views here.
#DataFlair #Send Email
def register(request):
    #sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'ACCOUNT ACTIVATION'
        message = 'Click the below link to activate your account'
        recepient = str(sub['email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        #return render(request, 'subscribe/success.html', {'recepient': recepient})
    #return render(request, 'subscribe/index.html', {'form':sub})