from django.shortcuts import render
from .models import Profile
from .forms import ProfileModeForm
# Create your views here.

def my_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileModeForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True

    context = {
        'profile': profile,
        'form': form,
        'confirm': confirm,
    }
    return render(request, 'profiles/myprofile.html', context)
