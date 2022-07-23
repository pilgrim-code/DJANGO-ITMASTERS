
from django.shortcuts import render,HttpResponse
from App.Models.User_forms import SignUpForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth

class UserController():
    
    def register(request):
        template = 'views/user/register.html'
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                dataEmail = None
                email = form.cleaned_data.get('email')
               # user = form.cleaned_data.get('usuario')
               
                userdb = User.objects.filter(email=email)
               # userdb = User.objects.all()
                for item in userdb:
                    print(item)
                    dataEmail=item.email
                  #  dataUser = item.user
                    print(dataEmail)
                   # print(dataUser)
                    
                if dataEmail != None:
                    context = {'form':form ,'error':'El correo ya esta registrado, prueba con otro' }
                    return render(request,template,context)
                #elif dataUser == user:
               #     context = {'form':form ,'error':'El Usuario ya esta registrado, prueba con otro' }
                #    return render(request,template,context)
                    
                else:
                    nombre = form.cleaned_data.get('nombre')
                    apellido = form.cleaned_data.get('apellido')
                    usuario = form.cleaned_data.get('usuario')
                    email = form.cleaned_data.get('email')
                    contra = form.cleaned_data.get('contra')
                    User.objects.create_user(username=usuario,
                                             first_name=nombre,
                                             last_name=apellido,
                                             email=email,
                                             password=contra,
                                             is_staff=1
                                             )
                    user = auth.authenticate(username=usuario,password=contra)
                    auth.login(request,user)
                    return HttpResponseRedirect("admin/")
            else:
                context = {'form': form}
                return render(request,template,context)
            
        else:
            context = {'form': SignUpForm()}
        return render(request,template, context)
        