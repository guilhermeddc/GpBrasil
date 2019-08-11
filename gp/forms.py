import django.forms

from gp.models import *


class CityForm(django.forms.forms.Form):
    state = django.forms.ModelChoiceField(queryset=ChoicesStates.objects.all())
    city = django.forms.ModelChoiceField(queryset=ChoicesCity.objects.filter(state=7))


class SearchClientForm(django.forms.forms.Form):
    genre = django.forms.ModelMultipleChoiceField(queryset=ChoicesGenre.objects.all(),
                                                  required=False,
                                                  widget=django.forms.CheckboxSelectMultiple())
    eye = django.forms.ModelMultipleChoiceField(queryset=ChoicesEyeColor.objects.all(),
                                                required=False,
                                                widget=django.forms.CheckboxSelectMultiple())
    ethnicity = django.forms.ModelMultipleChoiceField(queryset=ChoicesEthnicity.objects.all(),
                                                      required=False,
                                                      widget=django.forms.CheckboxSelectMultiple())