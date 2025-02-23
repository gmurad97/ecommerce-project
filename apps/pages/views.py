from django.shortcuts import render

from .models import Setting


# Create your views here.
def index(request):
    # "settings": Setting.objects.first(), - check this line try catche exception....if object exitst this object send error

    context = {
        "settings": Setting.objects.first(),
    }
    return render(request, "pages/index.html", context)


def error_404(request, exception):
    pass
