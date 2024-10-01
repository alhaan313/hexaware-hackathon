from django import template

register = template.Library()

@register.filter
def filter_by_module(user_progress, module_id):
    # If user_progress is None or empty, return False (no progress)
    if not user_progress:
        return False
    return user_progress.filter(module__id=module_id).exists()