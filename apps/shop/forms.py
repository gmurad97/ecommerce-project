from django import forms
from .models import Product
from .widgets import MultiFileInput


class ProductForm(forms.ModelForm):
    images = forms.FileField(
        widget=MultiFileInput(attrs={"multiple": True}), required=False
    )

    class Meta:
        model = Product
        fields = ["images"]

    def save(self, commit=True):
        instance = super().save(commit=False)
        uploaded_files = self.files.getlist("images")

        paths = []
        for f in uploaded_files:
            from django.core.files.storage import default_storage

            path = default_storage.save(f"uploads/{f.name}", f)
            paths.append(path)

        instance.images = paths

        if commit:
            instance.save()
        return instance
