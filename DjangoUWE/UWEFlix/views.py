from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from UWEFlix.models import ManageAccount
from UWEFlix.forms import ManageAccountsForm
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

#home page function, displayed as default logout page 
def home(request):
    return render(request, 'UWEFlix/home.html')

#user login function
def user_login(request):
    if request.method == 'POST':
        #process the request
        username = request.POST['username']
        password = request.POST['password']
        #check for correct username and password
        user = authenticate(username=username, password=password)
        if user is not None:
            #save session for login
            login(request, user)
            #redirects successfully logged in user to ManageAccountList page
            return ManageAccountsList(request)
        else:
            #if username or password incorrect an error message is displayed
            return render(request, 'UWEFlix/login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        #login page is displayed if no POST data is available
        return render(request, 'UWEFlix/login.html')

#manage accounts list function to display table of data from database
#search bar allows user to search by name
@ csrf_protect
@ csrf_exempt
def ManageAccountsList(request):
    #accounts = ManageAccounts.objects.all() ->dsplays all without filter option
    search_query = ""
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    accounts = ManageAccount.objects.filter(
        Q(acc_name__icontains=search_query)
    )

    context = {
        'accounts': accounts,
        'search_query': search_query,
    }
    return render(request, 'UWEFlix/ManageAccountsList.html', context)

#create a new account function, this function is used once the form is valid
def ManageAccountsCreate(request):
    form = ManageAccountsForm()

    if request.method == 'POST':
        form = ManageAccountsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ManageAccountsList')
    context = {
        'form': form,
    }
    return render(request, 'UWEFlix/ManageAccountsCreate.html', context)

#edit account information function
def ManageAccountsEdit(request, pk):
    account = ManageAccount.objects.get(id=pk)
    form = ManageAccountsForm(instance=account)

    if request.method == 'POST':
        form = ManageAccountsForm(request.POST, request.FILES, instance=account)
        if form.is_valid():
            form.save()
            return redirect('ManageAccountsList')
    context = {
        'account': account,
        'form': form,
    }
    return render(request, 'UWEFlix/ManageAccountsEdit.html', context)

#delete account information function
def ManageAccountsDelete(request, pk):
    account = ManageAccount.objects.get(id=pk)

    if request.method == 'POST':
        account.delete()
        return redirect('ManageAccountsList')
    context = {
        'account':account,
    }
    return render(request, 'UWEFlix/ManageAccountsDelete.html', context)

