from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from . import MiniSiteNameSpace


class OpportunityPage(MiniSiteNameSpace):
    """
    these pages come with sign-up-for-xyz CTAs
    """
    cta = models.ForeignKey(
        'Signup',
        related_name='page',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text='Choose existing or create new petition form'
    )

    content_panels = Page.content_panels + [
        FieldPanel('header'),
        SnippetChooserPanel('cta'),
        StreamFieldPanel('body'),
    ]

    subpage_types = [
        'OpportunityPage',
        'RedirectingPage',
    ]
