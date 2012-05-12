import copy 
from templer.core.base import get_var
from templer.zope import abstract_zope


class NestedZope(abstract_zope.AbstractNestedZope):
    _template_dir = 'templates/nested_zope'
    summary = "A nested-namespace Zope package"
    help = """
This creates a Zope package with a nested (2-dot) namespace 
(like 'my.nested.package').
"""
    required_templates = ['nested_namespace']
    default_required_structures = ['egg_docs', 'bootstrap',]
    use_cheetah = True
    vars = copy.deepcopy(abstract_zope.AbstractNestedZope.vars)
    get_var(vars, 'namespace_package').default = 'myzopelib'
    get_var(vars, 'package').default = 'example'
    