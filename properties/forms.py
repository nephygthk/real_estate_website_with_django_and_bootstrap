from django import forms
from django.forms.models import inlineformset_factory


from .models import Property, Media


class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = '__all__'
        exclude = ['created', 'updated', 'slug']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})



MediaFormSet = inlineformset_factory(Property, Media, extra=1, fields =['property_image',])
