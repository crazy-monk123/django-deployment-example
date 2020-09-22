from django import template


register=templates.Library()

def cut(value,arg):
    """
    This cuts out all value of args from the string
    """

    return value.replace(arg,'')


register.filter('cut',cut)
