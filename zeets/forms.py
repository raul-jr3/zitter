from django import forms


from .models import Zeet, Comment

class ZeetPostForm(forms.ModelForm):
	class Meta:
		model = Zeet
		fields = ['body', 'image']


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['body']