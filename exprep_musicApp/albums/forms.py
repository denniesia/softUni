from django import forms
from .models import Album
from exprep_musicApp.mixins import PlaceholderMixin, ReadOnlyMixin


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['owner',]

class AlbumCreateForm(PlaceholderMixin, AlbumBaseForm):
    pass

class AlbumEditForm(PlaceholderMixin, AlbumBaseForm):
    pass

class AlbumDeleteForm(ReadOnlyMixin, AlbumBaseForm):
    read_only_fields = ['name', 'artist', 'genre', 'price', 'description']
