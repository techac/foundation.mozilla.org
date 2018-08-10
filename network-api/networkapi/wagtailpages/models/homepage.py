from django.conf import settings
from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, FieldRowPanel, InlinePanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmetadata.models import MetadataPageMixin


class Homepage(MetadataPageMixin, Page):
    hero_headline = models.CharField(
        max_length=140,
        help_text='Hero story headline',
        blank=True,
    )

    hero_story_description = RichTextField(
        features=[
            'bold', 'italic', 'link',
        ]
    )

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='hero_image'
    )

    hero_button_text = models.CharField(
        max_length=50,
        blank=True
    )

    hero_button_url = models.URLField(
        blank=True
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_headline'),
            FieldPanel('hero_story_description'),
            FieldRowPanel([
                FieldPanel('hero_button_text'),
                FieldPanel('hero_button_url'),
            ]),
            ImageChooserPanel('hero_image'),
        ],
            heading='hero',
            classname='collapsible'
        ),
        InlinePanel('featured_highlights', label='Highlights', max_num=5),
        InlinePanel('featured_news', label='News', max_num=4),
    ]

    subpage_types = [
        'PrimaryPage',
        'PeoplePage',
        'InitiativesPage',
        'Styleguide',
        'NewsPage',
        'ParticipatePage',
        'MiniSiteNameSpace',
        'RedirectingPage',
        'OpportunityPage',
    ]

    def get_context(self, request):
        # We need to expose MEDIA_URL so that the s3 images will show up properly
        # due to our custom image upload approach pre-wagtail
        context = super(Homepage, self).get_context(request)
        print(settings.MEDIA_URL)
        context['MEDIA_URL'] = settings.MEDIA_URL
        return context
