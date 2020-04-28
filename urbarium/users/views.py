from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

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
            messages.success(request, f'Account created for {username}!')
            return redirect('character:index')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
