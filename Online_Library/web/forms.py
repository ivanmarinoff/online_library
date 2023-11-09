from django import forms

from Online_Library.web.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
class ProfileCreateForm(ProfileBaseForm):
    pass

class ProfileEditForm(ProfileBaseForm):
    pass

class ProfileDeleteForm(forms.ModelForm):
    pass

class BookCreateForm(forms.ModelForm):
    pass

class BookEditForm(forms.ModelForm):
    pass

class BookDeleteForm(forms.ModelForm):
    pass