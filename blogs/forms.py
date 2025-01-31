from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    tag_input=forms.CharField(required=False,help_text="Multiple tags, seperate by commas",label="Tag")
    class Meta:
        model=Post
        fields=['title','content','category','tag_input','image','published']
        labels={'published':'Publish',}
        help_texts={'published':"Tick, if you want to publish now",}
        


class CommentsForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['text',]
        labels={'text':"Comment below"}
        widgets={'text':forms.Textarea(attrs={'cols':10,'rows':5,})}
