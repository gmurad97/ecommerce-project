from django.forms.widgets import FileInput

class MultiFileInput(FileInput):
    allow_multiple_selected = True

    def value_from_datadict(self, data, files, name):
        return files.getlist(name)
