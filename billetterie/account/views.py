from django.shortcuts import render, redirect

from .models import Account
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from .forms import UserCreation

from django.contrib.auth.decorators import login_required



def Inscription(request):
    if request.user.is_authenticated:
        return redirect('compte')
    else:
        form = UserCreation()

        if request.method == 'POST':
            form = UserCreation(request.POST)

            if form.is_valid():
                email = form.cleaned_data['email']
                fist_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                password1 = form.cleaned_data.get('password1')
                username = form.cleaned_data.get('username')

                contact = Account.objects.filter(email=email)
                if not contact.exists():
                    # form.save()
                    if not contact.exists():
                        # If a contact is not registered, create a new one.
                        form.save()
                        """contact = User.objects.create_user(
                            username=username,
                            email=email,
                            first_name=fist_name,
                            last_name=last_name,
                            password=password1,
                        )"""
                    messages.success(request, 'Account was created for ' + email)

                    return redirect('connexion')
                else:
                    messages.info(request, 'Contact is exit')
                    return redirect('inscription')
        context = {'form': form,
                   'errors': form.errors.items()
                   }
    return render(request, 'htmlPages/connexion.html', context)


def Connexion(request):
    if request.user.is_authenticated:
        return redirect('compte')
    else:
        if request.method == 'POST':
            email = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('acceuil')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
    return render(request, 'htmlPages/connexion.html', context)



def Connexionadmin(request):
    if request.user.is_authenticated:
        return redirect('nameadmin:admin')
    else:
        if request.method == 'POST':
            email = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                if user.is_admin == True:
                    login(request, user)
                    return redirect('nameadmin:admin')
                else:
                    messages.info(request, "Vous n'est pas autoriser à vous connecter :( ")
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
    return render(request, 'htmlPages/connexion.html', context)


def logoutUser(request):
    logout(request)
    return redirect('connexion')