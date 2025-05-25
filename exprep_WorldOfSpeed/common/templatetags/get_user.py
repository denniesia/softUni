from exprep_WorldOfSpeed.utils import get_user_obj
from django import template

register = template.Library()
@register.simple_tag
def get_user():
    return get_user_obj()
