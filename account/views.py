from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout


User = get_user_model()


class Signin(View):
    template_name = ''

    def get_context_data(self, **kwargs):
        context = {
            "error_msg": ""
        }
        context['is_doctor'] = kwargs.get('is_doctor')
        context['is_patient'] = kwargs.get('is_patient')
        return context

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            is_doctor = kwargs.get('is_doctor')
            is_patient = kwargs.get('is_patient')
            context = self.get_context_data(
                is_doctor=is_doctor, is_patient=is_patient)
            return render(request, self.template_name, context)
        else:
            return redirect("Home")

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        is_doctor = kwargs.get('is_doctor')
        is_patient = kwargs.get('is_patient')
        context = self.get_context_data(
            is_doctor=is_doctor, is_patient=is_patient)

        if is_doctor == True:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("Home")
            else:
                context['error_msg'] = "Invalid Username and Password!!"

        if is_patient == True:
            if user:
                login(request, user)
                return redirect("Home")
            else:
                context['error_msg'] = "Invalid Username and Password!!"
        return render(request, self.template_name, context)


class Signup(View):
    template_name = ''

    def get_context_data(self, **kwargs):
        context = {
            'registration_success_msg': ""
        }
        context['is_doctor'] = kwargs.get('is_doctor')
        context['is_patient'] = kwargs.get('is_patient')
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        print(len(context['registration_success_msg']))
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        is_doctor = kwargs.get('is_doctor')
        is_patient = kwargs.get('is_patient')
        name = request.POST['first_name']
        username = request.POST['username']
        password = request.POST['password']
        context = self.get_context_data(
            is_doctor=is_doctor, is_patient=is_patient)

        if context['is_patient'] == True:
            user = User.objects.create_user(first_name=name, username=username,
                                            password=password, is_patient=True)
            user.save()
            context['registration_success_msg'] = "Patient Registration Succeffully"
        if context['is_doctor'] == True:
            user = User.objects.create_user(first_name=name, username=username,
                                            password=password, is_doctor=True, is_active=True)
            user.save()
            context['registration_success_msg'] = "Doctor Registration Succeffully"
        return render(request, self.template_name, context)
