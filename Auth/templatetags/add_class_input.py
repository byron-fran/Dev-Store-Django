from django import template

register = template.Library()

@register.filter
def add_class_input(field, className):
    return field.as_widget(attrs={'class' : className})