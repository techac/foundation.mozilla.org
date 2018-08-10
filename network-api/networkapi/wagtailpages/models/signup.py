from wagtail.snippets.models import register_snippet

from . import CTA


@register_snippet
class Signup(CTA):

    class Meta:
        verbose_name = 'signup snippet'
