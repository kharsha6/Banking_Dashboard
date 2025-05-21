from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import BankingInfo
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Transaction
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def dashboard_view(request):
    try:
        banking_info = BankingInfo.objects.get(user=request.user)
    except BankingInfo.DoesNotExist:
        banking_info = None

    return render(request, 'accounts/dashboard.html', {
        'banking_info': banking_info,
        'user': request.user
    })


def forgot_password_view(request):
    if request.method == 'POST':
        if 'username' in request.POST:
            username = request.POST.get('username')
            try:
                user = User.objects.get(username=username)
                return render(request, 'accounts/reset_password_form.html', {'username': username})
            except User.DoesNotExist:
                messages.error(request, 'Username does not exist.')
        elif 'new_password' in request.POST:
            username = request.POST.get('username')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if new_password != confirm_password:
                messages.error(request, 'Passwords do not match.')
                return render(request, 'accounts/reset_password_form.html', {'username': username})
            try:
                user = User.objects.get(username=username)
                user.password = make_password(new_password)
                user.save()
                messages.success(request, 'Password changed successfully. Please login.')
                return redirect('login')
            except User.DoesNotExist:
                messages.error(request, 'Something went wrong. Try again.')
    return render(request, 'accounts/forgot_password.html')

def reset_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'reset_password.html', {'username': username})

        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            messages.success(request, "Password reset successfully.")
            return redirect('login')  # 🔁 This will redirect to the login page
        except User.DoesNotExist:
            messages.error(request, "User does not exist.")
            return render(request, 'reset_password.html')

    return render(request, 'reset_password.html')



@login_required
def transactions_view(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'accounts/transactions.html', {
        'transactions': transactions
    })




class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
