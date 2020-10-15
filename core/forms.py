from allauth.socialaccount.forms import SignupForm
from django import forms
from django.core.exceptions import ValidationError

from .fields import TimeZoneFormField
from .models import *


class SignupFormWithTimezone(SignupForm):
    timezone = TimeZoneFormField(display_GMT_offset=True)

    def save(self, request):
        user = super(SignupFormWithTimezone, self).save(request)
        user.timezone = self.cleaned_data['timezone']
        user.save()
        return user


class JoinFleetForm(forms.Form):
    character = forms.ModelChoiceField(queryset=Character.objects.all(), initial=0)


class FleetForm(forms.Form):
    name = forms.CharField(max_length=100)
    fleet_type = forms.ModelChoiceField(queryset=FleetType.objects.all(), initial=0)
    description = forms.CharField(required=False)
    location = forms.CharField(required=False)
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'datepicker',
        },
            format='%b %d, %Y'
        ),
        input_formats=['%b %d, %Y'],
    )
    start_time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'class': 'timepicker',
        },
            format='%I:%M %p'
        ),
        input_formats=['%I:%M %p'],
    )
    expected_duration = forms.CharField(required=False,
                                        help_text="If you don't know how long guess here, otherwise fill in the two "
                                                  "fields below.")
    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'datepicker',
        },
            format='%b %d, %Y'
        ),
        input_formats=['%b %d, %Y'],
    )
    end_time = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={
            'class': 'timepicker',
        },
            format='%I:%M %p'
        ),
        input_formats=['%I:%M %p'],
    )

    def clean(self):
        cleaned_data = super().clean()
        end_date = cleaned_data.get("end_date")
        end_time = cleaned_data.get("end_time")

        if bool(end_date) != bool(end_time):
            raise ValidationError(
                "You must fill in both of the End Date and End Time fields."
            )


class SettingsForm(forms.ModelForm):
    timezone = TimeZoneFormField(display_GMT_offset=True)

    class Meta:
        model = GooseUser
        fields = ["timezone"]