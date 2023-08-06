from django import forms
from .models import Review
from .models import CallBack
from django.forms.widgets import RadioSelect
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'firstname',
            'lastname',
            'stars',
            'description',
        ]
        widgets = {
            'stars': forms.RadioSelect(choices=[(i, i) for i in range(1, 6)])
        }
        

class CallBackForm(forms.ModelForm):
    class Meta:
        model = CallBack
        fields = [
            'email',
            'number',
            'message'
        ]
        
