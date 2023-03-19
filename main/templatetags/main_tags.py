from django import template
from main.models import Post
from datetime import date

register = template.Library()

@register.filter
def compare_dates(value):
    return (value - date.today()).days