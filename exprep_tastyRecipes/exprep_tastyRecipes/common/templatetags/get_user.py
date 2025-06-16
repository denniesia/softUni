from django import template
from exprep_tastyRecipes.utils import get_user_obj

register = template.Library()

@register.simple_tag(name='get_user')
def get_user():
    return get_user_obj()