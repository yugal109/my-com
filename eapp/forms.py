from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Firstname'
        self.fields['first_name'].widget.attrs['id'] = 'Firstname'

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Lastname'
        self.fields['last_name'].widget.attrs['id'] = 'Lastname'

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].widget.attrs['id'] = 'username'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['id'] = 'email'
        self.fields['email'].widget.attrs['name'] = 'email'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['id'] = 'pass1'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs[
            'placeholder'] = 'Confirm Password'
        self.fields['password2'].widget.attrs['id'] = 'pass2'


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ["comment"]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs['class'] = 'form-control'
        self.fields['comment'].widget.attrs['name'] = 'comment'
        self.fields['comment'].widget.attrs['placeholder'] = 'Review Here'


class RatingForm(forms.ModelForm):
    class Meta:
        model = RatingModel
        fields = ["rating"]

    def __init__(self, *args, **kwargs):
        super(RatingForm, self).__init__(*args, **kwargs)

        self.fields['rating'].widget.attrs['class'] = 'form-control'
        self.fields['rating'].widget.attrs['id'] = 'rate'


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ["question"]

    def __init__(self, *args, **kwargs):
        super(QuestionsForm, self).__init__(*args, **kwargs)

        self.fields['question'].widget.attrs['class'] = 'form-control'
        self.fields['question'].widget.attrs['placeholder'] = 'Write Question here'


class OrderItemsForm(forms.ModelForm):
    class Meta:
        model = OrderItems
        fields = ["quantity"]

    def __init__(self, *args, **kwargs):
        super(OrderItemsForm, self).__init__(*args, **kwargs)

        self.fields['quantity'].widget.attrs['class'] = 'form-control'
        self.fields['quantity'].widget.attrs['name'] = 'quantity'
        self.fields['quantity'].widget.attrs['id'] = 'quantity'
        self.fields['quantity'].widget.attrs['min'] = 1
        self.fields['quantity'].widget.attrs['value'] = 1


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedbacks
        fields = ["email", "feedback"]

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['id'] = 'email'
        self.fields['email'].widget.attrs['placeholder'] = 'E-Mail'
        self.fields['feedback'].widget.attrs['placeholder'] = 'Feedback'
        self.fields['feedback'].widget.attrs['id'] = 'feedback'
        self.fields['feedback'].widget.attrs['class'] = 'form-control'
