from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class InitiativeSection(models.Model):
    page = ParentalKey(
        'wagtailpages.InitiativesPage',
        related_name='initiative_sections',
    )

    sectionImage = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='section_image',
        verbose_name='Hero Image',
    )

    sectionHeader = models.CharField(
        verbose_name='Header',
        max_length=250,
    )

    sectionCopy = models.TextField(
        verbose_name='Subheader',
    )

    sectionButtonTitle = models.CharField(
        verbose_name='Button Text',
        max_length=250,
    )

    sectionButtonURL = models.TextField(
        verbose_name='Button URL',
    )

    panels = [
        ImageChooserPanel('sectionImage'),
        FieldPanel('sectionHeader'),
        FieldPanel('sectionCopy'),
        FieldPanel('sectionButtonTitle'),
        FieldPanel('sectionButtonURL'),
    ]
