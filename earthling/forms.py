from .models import *
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='パスワードの確認', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'is_adviser', 'birth', 'gender', 'is_admin')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("パスワードが間違っています")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password',
                  'is_active', 'is_admin', 'username', 'first_name', 'last_name', 'is_adviser', 'birth', 'gender')

    def clean_password(self):
        return self.initial["password"]

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'gender')

    def clean_password(self):
        return self.initial["password"]

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text='必須  有効なメールアドレスを入力してください。',
        label='Eメールアドレス',
    )

    username = forms.CharField(
        max_length=30,
        required=True,
        help_text='必須',
        label='ユーザーネーム'
    )

    last_name = forms.CharField(
        max_length=20,
        required=True,
        help_text="必須",
        label='性'
    )

    first_name = forms.CharField(
        max_length=20,
        required=True,
        help_text="必須",
        label='名'
    )

    birth = forms.DateField(
        widget=forms.SelectDateWidget(),
        required=True,
        help_text='必須',
        label='生年月日'
    )

    GENDER = (
        ("男性", "男性"),
        ("女性", "女性"),
        ("その他", "その他")
    )
    gender = forms.ChoiceField(
        choices=GENDER,
        required=True,
        help_text='必須',
        label='性別'
    )

    is_adviser = forms.BooleanField(
        required=False,
        label='アドバイザーとして登録する場合はチェックを入れてください',
    )
    

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'birth', 'gender', 'is_adviser', 'password1', 'password2', )
    
    def __init__(self, year, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if year != None:
            self.fields["birth"].widget = forms.SelectDateWidget(years=range(1910, year))

class AdviserEditForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Adviser
        fields = ('height', 'profile', 'is_active', 'profile_pic', 'instagram', 'wear', 'tiktok', 'twitter', 'facebook', 'hp')

class LoginForm(forms.Form):
    email = forms.CharField(label='メールアドレス', max_length=30)
    password = forms.CharField(
            label='パスワード', max_length=128, widget=forms.PasswordInput())

class ReviewForm(forms.ModelForm):   
    class Meta:
        model = Review
        fields = ['score', 'comment']