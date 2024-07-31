from django import forms


class Filters(forms.Form):
    price_range = forms.IntegerField(max_value=150000)
    size = forms.CharField(max_length=2)
    kind = forms.CharField(max_length=32)
    sex = forms.CharField(max_length=6)
    creator = forms.CharField(max_length=32)


    def clean_price_range(self):
        if self.cleaned_data['price_range']:
            try:
                return int(self.cleaned_data['price_range'])
            except:
                raise forms.ValidationError('Weird. Why you try broke my filter :(')

        else:
            return None

    def clean_size(self):
        if self.cleaned_data['size']:
            try:
                return int(self.cleaned_data['size'])
            except:
                raise forms.ValidationError('Oh. Stop broke my filters')

        else:
            return None

    def clean_kind(self):
        if self.cleaned_data['kind']:
            try:
                return str(self.cleaned_data['kind'])
            except:
                raise forms.ValidationError('You again...')
        else:
            return None

    def clean_sex(self):
        if self.cleaned_data['sex']:
            if self.cleaned_data['sex'] not in ['women', 'man']:
                raise forms.ValidationError('Are you kidding?')
        else:
            return None

    def clean_creator(self):
        if self.cleaned_data['creator']:
            try:
                return str(self.cleaned_data['creator'])
            except:
                raise forms.ValidationError('HEHHE. No.')

        else:
            return None
