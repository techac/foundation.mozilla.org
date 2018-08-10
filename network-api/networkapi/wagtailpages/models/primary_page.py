from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtailmetadata.models import MetadataPageMixin

from . import base_fields
from networkapi.wagtailpages.utils import get_page_tree_information


class PrimaryPage(MetadataPageMixin, Page):
    """
    Basically a straight copy of modular page, but with
    restrictions on what can live 'under it'.

    Ideally this is just PrimaryPage(ModularPage) but
    setting that up as a migration seems to be causing
    problems.
    """
    header = models.CharField(
        max_length=250,
        blank=True
    )

    narrowed_page_content = models.BooleanField(
        default=False,
        help_text='For text-heavy pages, turn this on to reduce the overall width of the content on the page.'
    )

    zen_nav = models.BooleanField(
        default=False,
        help_text='For secondary nav pages, use this to collapse the primary nav under a toggle hamburger.'
    )

    body = StreamField(base_fields)

    settings_panels = Page.settings_panels + [
        MultiFieldPanel([
            FieldPanel('narrowed_page_content'),
        ]),
        MultiFieldPanel([
            FieldPanel('zen_nav'),
        ])
    ]

    content_panels = Page.content_panels + [
        FieldPanel('header'),
        StreamFieldPanel('body'),
    ]

    parent_page_types = [
        'Homepage',
        'PrimaryPage',
    ]

    subpage_types = [
        'PrimaryPage',
        'RedirectingPage'
    ]

    show_in_menus_default = True

    def get_context(self, request, *args, **kwargs):
        context = super(PrimaryPage, self).get_context(request)
        return get_page_tree_information(self, context)
