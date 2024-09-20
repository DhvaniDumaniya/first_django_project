from django import forms
from .models import thing  # Make sure to import your model

class thingForm(forms.ModelForm):
    class Meta: #This inner class provides metadata to the form. It tells Django which model to use and which fields to include
        model = thing
        fields = '__all__'  # Specify the fields you want to include

