from django import template
from django.utils.safestring import mark_safe
from django_bootstrap5.components import render_button
register = template.Library()

@register.simple_tag
def isu22_button(content, **kwargs):
    content += mark_safe("<span class='arrow'></span>")
    button_class = kwargs.get("button_class", "")
    button_class = " iastate22-button" + button_class
    kwargs['button_class'] = button_class
    return render_button(content, **kwargs)