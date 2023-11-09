from django.shortcuts import render, redirect

from Online_Library.web.forms import ProfileCreateForm
from Online_Library.web.models import Profile


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


# Create your views here.
def index(request):
    return render(request, 'home-no-profile.html')


def add_book(request):
    return render(request, 'add-book.html')


def edit_book(request, pk):
    return render(request, 'edit-book.html')


def details_book(request, pk):
    return render(request, 'book-details.html')


def add_profile(request):
    profile = get_profile()
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    return render(request, 'edit-profile.html')


def delete_profile(request):
    return render(request, 'delete-profile.html')
