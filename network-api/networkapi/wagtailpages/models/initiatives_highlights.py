from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.core.models import Orderable as WagtailOrderable
from wagtail.snippets.edit_handlers import SnippetChooserPanel


class InitiativesHighlights(WagtailOrderable, models.Model):
    page = ParentalKey(
        'wagtailpages.InitiativesPage',
        related_name='featured_highlights',
    )
    highlight = models.ForeignKey('highlights.Highlight', related_name='+')
    panels = [
        SnippetChooserPanel('highlight'),
    ]

    class Meta:
        verbose_name = 'highlight'
        verbose_name_plural = 'highlights'
        ordering = ['sort_order']  # not automatically inherited!

    def __str__(self):
        return self.page.title + '->' + self.highlight.title
