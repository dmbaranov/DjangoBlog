from django import template

register = template.Library()


@register.simple_tag
def query_transform(request, **kwargs):
    updated = request.GET.copy()

    for item in kwargs:
        updated[item] = kwargs[item]

    return updated.urlencode()
