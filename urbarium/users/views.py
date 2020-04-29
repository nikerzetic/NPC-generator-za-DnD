from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Options for messages:
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error


def register(request):
    # Was the request a post request?
    if request.method == 'POST':
        # creates a form with the data from within the post
        form = UserRegisterForm(request.POST)
        # Check if the data (=username, password,...) is valid
        if form.is_valid():
            # save the form
            form.save()
            # Now you can get the data from the POST request
            # The data is in a dictionary called cleaned_data
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# A decorator that makes it so that the user has to be logged in to view this page
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')    
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
