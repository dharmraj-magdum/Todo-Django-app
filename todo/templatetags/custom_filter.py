from django import template

register = template.Library()

priority_choices = [
    "low",
    "Medium",
    "High",
]


@register.filter(name='priority_text')
def integerToText(num):
    num = int(num)-1
    # print(num)
    return priority_choices[num]
