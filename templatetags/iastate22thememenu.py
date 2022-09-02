from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='render_menu_item')
def render_menu_item(menu_item, level=0):
    if menu_item.children:
        template = """
        <li>
            <a href="{}">
                {}
            </a>
            <ul>
                {}
            </ul>
        </li>"""
        return mark_safe(template.format(menu_item.url, menu_item.text, "".join([render_menu_item(item, level+1) for item in menu_item.children])))
    else:
        template = """
                    <li>
                        <a href="{}">
                            {}
                        </a>
                    </li>"""
        return mark_safe(template.format(menu_item.url, menu_item.text))