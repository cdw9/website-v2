from django.forms import Form, ModelChoiceField, ModelForm

from versions.models import Version
from .models import Library


class LibraryForm(ModelForm):
    class Meta:
        model = Library
        fields = ["categories"]


class VersionSelectionForm(Form):
    # Remove non released versions from the queryset.
    queryset = Version.objects.active().defer("data")

    version = ModelChoiceField(
        queryset=queryset,
        label="Select a version",
        empty_label="Choose a version...",
    )
