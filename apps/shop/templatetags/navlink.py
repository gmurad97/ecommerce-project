from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag(name="navlink")
def navlink(*, request, url_name, active_class="active", exact_match=False, **kwargs) -> str:
    current_url = request.path
    target_url = reverse(url_name, kwargs=kwargs)
    return active_class if (current_url == target_url if exact_match else current_url.startswith(target_url)) else ""
