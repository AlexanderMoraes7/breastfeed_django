from django import template

register = template.Library()

class BlockNotOverriddenError(NotImplementedError):
    pass

@register.simple_tag
def ensure_overridden():
    '''
    Use inside a base.html block to ensure that will be override.
    Use dentro de um bloco em base.html para garantir que será sobrescrito.
    '''
    raise BlockNotOverriddenError(
            'This Block need to be override in a son template.\n'
            'Esse Bloco deve ser sobrescrito em um template filho'
    )
