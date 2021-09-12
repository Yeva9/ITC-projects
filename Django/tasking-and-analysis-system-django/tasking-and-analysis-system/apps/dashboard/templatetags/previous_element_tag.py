from django import template

register = template.Library()

@register.filter
def previous(some_list, current_index):
    """
    This function returns the previous element of the list using the current index if it exists.
    Otherwise returns an empty string.
    """
    try:
        some_list = list(some_list)
        return some_list[int(current_index) - 1] # access the previous element

    except:
        return ' ' # return empty string in case of exception