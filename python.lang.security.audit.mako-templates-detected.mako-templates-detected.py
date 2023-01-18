from mako.template import Template
from mako import template
import mako
import jinja2
# ruleid:mako-templates-detected
mako.template.Template("hern")
template.Template("hern")
Template("hello")
# ok:mako-templates-detected
t = jinja2.Template("Hello {{ name }}")
t.render(name="world!")
