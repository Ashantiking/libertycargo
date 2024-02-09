
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.generic import View
import json
# from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage
from django.urls import reverse
from django.contrib import auth
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError

# from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator
# Create your views here.


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid. Please cheeck your email and try again'}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Email Already Taken, Please try  another'}, status=409)

        return JsonResponse({'email_vaild': True})


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Username Already Taken, Choose another'}, status=409)

        return JsonResponse({'username_vaild': True})


class RegisterView(View):
    def get(self, request):
        return render(request, 'registration/register.html', {})
        # success_url = reverse_lazy('login')

    def post(self, request):
        # Get User Data
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            'fieldValues': request.POST
        }

        # Validate
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():

                if len(password) < 6:
                    messages.error(request, 'Password is too short')
                    return render(request, 'registration/register.html', context)

                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_activate = False
                user.save()

                # path_to_view
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                # -get the domain we are on
                domain = get_current_site(request).domain
                link = reverse('activate', kwargs={
                    'uidb64': uidb64, 'token': token_generator.make_token(user)})

                # -relative url to verifacations
                activate_url = 'http://'+domain+link

                email_subject = 'Activate your account'
                email_body = 'Hi' + user.username + \
                    'Please use this link to verify your account\n' + activate_url
                email = EmailMessage(
                    email_subject,
                    email_body,
                    'livenkacheampong@acheampong.com',
                    [email],
                )
                email.send(fail_silently=False)
                messages.success(request, 'Account successfully created')
                return render(request, 'registration/register.html', {})

        return render(request, 'registration/register.html', {})

        # Create a User Account


class VerificationView(View):
    def get(self, request, uidb64, token):

        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_actvation_token.check_token(user, token):
                return redirect('login'+'?message='+'User is already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')

        except Expression as ex:
            pass

        return redirect('login')


class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html', {})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                if user .is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome ' +
                                     user.username + 'Your are now login')
                    return redirect("index")
                messages.error(
                    request, 'Account is not activate, Please check your email')
                return render(request, 'registration/login.html')

            messages.error(
                request, 'Invaild credentials, Please try again')
            return render(request, 'registration/login.html')

        messages.error(
            request, 'Please all fields')
        return render(request, 'registration/login.html')
