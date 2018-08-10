from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.core.models import Orderable as WagtailOrderable
from wagtail.snippets.edit_handlers import SnippetChooserPanel


class HomepageFeaturedNews(WagtailOrderable, models.Model):
    page = ParentalKey(
        'wagtailpages.Homepage',
        related_name='featured_news',
    )
    news = models.ForeignKey('news.News', related_name='+')
    panels = [
        SnippetChooserPanel('news'),
    ]

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
        ordering = ['sort_order']  # not automatically inherited!

    def __str__(self):
        return self.page.title + '->' + self.news.headline
