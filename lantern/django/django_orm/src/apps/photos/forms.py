from apps.photos.models import Photo
from django.forms import models


class UploadPhotoForm(models.ModelForm):
    class Meta:
        model = Photo
        fields = "__all__"
