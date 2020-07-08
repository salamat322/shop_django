from django import forms


QUANTITY = [(i, str(i)) for i in range(1, 11)]


class AddToCartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=QUANTITY, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
