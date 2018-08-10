from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from . import PrimaryPage


class InitiativesPage(PrimaryPage):
    parent_page_types = ['Homepage']
    template = 'wagtailpages/static/initiatives_page.html'

    subpage_types = [
        'MiniSiteNameSpace',
        'RedirectingPage',
        'OpportunityPage',
    ]

    primaryHero = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='primary_hero',
        verbose_name='Primary Hero Image',
    )

    subheader = models.TextField(
        blank=True,
    )

    h3 = models.TextField(
        blank=True,
    )

    sub_h3 = models.TextField(
        blank=True,
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('primaryHero'),
        FieldPanel('header'),
        FieldPanel('subheader'),
        FieldPanel('h3'),
        FieldPanel('sub_h3'),
        InlinePanel('initiative_sections', label="Initiatives"),
        InlinePanel('featured_highlights', label='Highlights', max_num=9),
    ]
