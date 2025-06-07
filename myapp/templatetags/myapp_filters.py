from django import template
register = template.Library()

@register.filter
def zip_lists(lists_tuple):
    return zip(*lists_tuple)