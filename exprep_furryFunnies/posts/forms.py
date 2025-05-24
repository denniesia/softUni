from django import forms
from .models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ('title', 'image_url', 'content', )
        labels = {
            'title': 'Title:',
            'image_url': 'Post Image URL:',
            'content': 'Content:',
        }
        widgets = {
            'title':forms.TextInput(attrs={'placeholder':'Put an attractive and unique title...'}),
            'content': forms.Textarea(attrs={'placeholder':'Share some interesting facts about your adorable pets...'}),
        }
        help_texts = {
            'image_url': 'Share your funniest furry photo URL!',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].error_messages['unique'] = (
            "Oops! That title is already taken. How about something fresh and fun?"
        )


