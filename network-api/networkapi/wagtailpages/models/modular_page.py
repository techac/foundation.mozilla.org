from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtailmetadata.models import MetadataPageMixin

from . import base_fields


class ModularPage(MetadataPageMixin, Page):
    """
    The base class offers universal component picking
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
        default=True,
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

    # Legacy field for now, necessary to make sure that the
    # actualy <title> element has the correct value in it.
    # This uses page.meta_title in the base.html
    # master template, which is still based on Mezzanine
    # page models, rather than Wagtail pages models.
    @property
    def meta_title(self):
        return self.title

    show_in_menus_default = True

    class Meta:
        app_label = 'wagtailpages'
