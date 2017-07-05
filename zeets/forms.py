from django import forms


from .models import Zeet

class ZeetPostForm(forms.ModelForm):
	class Meta:
		model = Zeet
		fields = ['body', 'image']
