from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
from django.http import JsonResponse


from .decorators import (
    not_logged_in_required
)
from .forms import (
    UserRegistrationForm,
    LoginForm,
    UserProfileUpdateForm,
    PremiumAccessRequestForm,
    ProfilePictureUpdateForm


)
from .models import User, UserProfile


# Create your views here.
def home(request):
    # Your view code here...
    return render(request, 'index.html')


# def home2(request):
#     # Your view code here...
#     return render(request, 'home2.html')

def home2_view(request):
    # If the user is not authenticated, maybe redirect them to the login page
    if not request.user.is_authenticated:
        return redirect('login')

    # Check the user's premium access status
    if request.user.userprofile.is_premium_user == "PENDING":
        # Redirect to a different page or render a different template
        return render(request, 'pending_access.html')

    # If none of the above conditions are met, render the home2 page
    return render(request, 'home2.html')


# def home2(request):
#     # Your view code here...
#     return render(request, 'home.html')

# @csrf_protect
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             # return redirect to your home page or some other page after successful login
#             return redirect('home')
#         else:
#             return render(request, 'login.html', {'error': 'Invalid credentials'})

#     # If request is not POST, it will render login page
#     return render(request, 'login.html')


@never_cache
@not_logged_in_required
def login_user(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect('home2')
            else:
                messages.warning(request, "Wrong credentials")

    context = {
        "form": form
    }
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


@never_cache
@not_logged_in_required
def register_user(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            messages.success(request, "Registration sucessful")
            return redirect('login')

    context = {
        "form": form
    }
    return render(request, 'registration.html', context)


@login_required(login_url='login')
def profile(request):
    account = get_object_or_404(User, pk=request.user.pk)
    form = UserProfileUpdateForm(instance=account)

    if request.method == "POST":
        if request.user.pk != account.pk:
            return redirect('home2')

        form = UserProfileUpdateForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile has been updated sucessfully")
            return redirect('profile')
        else:
            print(form.errors)

    context = {
        "account": account,
        "form": form
    }
    return render(request, 'profile.html', context)


@never_cache
@not_logged_in_required
def register_user(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()

            # Create UserProfile instance for this user
            UserProfile.objects.create(user=user)

            messages.success(request, "Registration successful")
            return redirect('login')

    context = {
        "form": form
    }
    return render(request, 'registration.html', context)


# @login_required(login_url='login')
# def request_premium_access(request):
#     try:
#         user_profile = UserProfile.objects.get(user=request.user)
#     except UserProfile.DoesNotExist:
#         # Handle the error (you could create a UserProfile here, or return an error message)
#         return HttpResponse('UserProfile does not exist')

#     user_profile = UserProfile.objects.get(user=request.user)
#     if request.method == 'POST':
#         form = PremiumAccessRequestForm(request.POST, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             # You can add code here to send an email to the admin.
#     else:
#         form = PremiumAccessRequestForm(instance=user_profile)
#     return render(request, 'request_premium_access.html', {'form': form})


@login_required(login_url='login')
def request_premium_access(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = PremiumAccessRequestForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your request for premium access has been submitted. Please wait for approval.")
            # or wherever you want to redirect them after the request
            # return redirect('home2')
            # Render the confirmation template instead of redirecting to 'home2'
            return render(request, 'request_confirmation.html')
    else:
        form = PremiumAccessRequestForm(instance=user_profile)
    return render(request, 'request_premium_access.html', {'form': form})


# @login_required(login_url='login')
# def some_view(request):
#     user_profile = UserProfile.objects.get(user=request.user)
#     if user_profile.is_premium_user == 'YES':
#         return render(request, 'premium_content.html')
#     else:
#         messages.warning(
#             request, "You do not have premium access yet. Please wait for approval.")
#         # or wherever you want to redirect them if they don't have
#         return redirect('home2')
@login_required(login_url='login')
def some_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    is_premium_user = user_profile.is_premium_user == 'YES'

    if is_premium_user:
        return render(request, 'premium_content.html', {'is_premium_user': is_premium_user})
    else:
        messages.warning(
            request, "You do not have premium access yet. Please wait for approval.")
        return redirect('home2')


@login_required
def change_profile_picture(request):
    if request.method == "POST":

        form = ProfilePictureUpdateForm(request.POST, request.FILES)

        if form.is_valid():
            image = request.FILES['profile_image']
            user = get_object_or_404(User, pk=request.user.pk)

            if request.user.pk != user.pk:
                return redirect('home')

            user.profile_image = image
            user.save()
            messages.success(request, "Profile image updated successfully")

        else:
            print(form.errors)

    return redirect('profile')


def view_user_information(request, username):
    account = get_object_or_404(User, username=username)
    following = False
    muted = None

    if request.user.is_authenticated:

        if request.user.id == account.id:
            return redirect("profile")

        followers = account.followers.filter(
            followed_by__id=request.user.id
        )
        if followers.exists():
            following = True

    if following:
        queryset = followers.first()
        if queryset.muted:
            muted = True
        else:
            muted = False

    context = {
        "account": account,
        "following": following,
        "muted": muted
    }
    return render(request, "user_information.html", context)


@login_required
def get_user_permission_status(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        is_premium_user = user_profile.is_premium_user == 'YES'
    except UserProfile.DoesNotExist:
        is_premium_user = False

    return JsonResponse({'is_premium_user': is_premium_user})
