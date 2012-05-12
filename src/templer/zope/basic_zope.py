import copy 
from templer.core.base import get_var
from templer.zope import abstract_zope


class BasicZope(abstract_zope.AbstractZope):
    _template_dir = 'templates/basic_zope'
    summary = "A Zope project"
    help = """
This creates a basic Zope package with a namespace (like 'my.package').
"""
    required_templates = ['basic_namespace']
    default_required_structures = ['egg_docs', 'bootstrap',]
    use_cheetah = True

    vars = copy.deepcopy(abstract_zope.AbstractZope.vars)
    get_var(vars, 'namespace_package').default = 'myzopelib'
    get_var(vars, 'package').default = 'example'


