from django.db import models
from wagtail.snippets.models import register_snippet

from .cta import CTA


@register_snippet
class Petition(CTA):
    legacy_petition = models.BooleanField(
        help_text='Mark this petition as a legacy petition in terms of where the data gets sent.',
        default=False,
    )

    campaign_id = models.CharField(
        max_length=20,
        help_text='Which campaign identifier should this petition be tied to?',
        null=True,
        blank=True,
    )

    requires_country_code = models.BooleanField(
        default=False,
        help_text='Will this petition require users to specify their country?',
    )

    requires_postal_code = models.BooleanField(
        default=False,
        help_text='Will this petition require users to specify their postal code?',
    )

    google_forms_url = models.URLField(
        help_text='Google form to post petition data to',
        max_length=2048,
        null=True,
        blank=True,
    )

    checkbox_1 = models.CharField(
        max_length=1024,
        help_text='label for the first checkbox option (may contain HTML)',
        blank=True,
    )

    checkbox_2 = models.CharField(
        max_length=1024,
        help_text='label for the second checkbox option (may contain HTML)',
        blank=True,
    )

    checkbox_1_form_field = models.CharField(
        max_length=1024,
        help_text='Google form field name for Checkbox 1',
        verbose_name='First checkbox Google Form field',
        blank=True,
    )

    checkbox_2_form_field = models.CharField(
        max_length=1024,
        help_text='Google form field name for Checkbox 1',
        verbose_name='Second checkbox Google Form field',
        blank=True,
    )

    given_name_form_field = models.CharField(
        max_length=1024,
        help_text='Google form field name for Given Name(s)',
        verbose_name='Given Name(s) Google Form field',
        blank=True,
    )

    surname_form_field = models.CharField(
        max_length=1024,
        help_text='Google form field name for Surname',
        verbose_name='Surname Google Form field',
        blank=True,
    )

    email_form_field = models.CharField(
        max_length=1024,
        help_text='Google form field name for Email',
        verbose_name='Email Google Form field',
        blank=True,
    )

    newsletter_signup_form_field = models.CharField(
        max_length=1024,
        help_text='Google form field name for Mozilla Newsletter checkbox',
        verbose_name='Mozilla Newsletter signup checkbox Google Form field',
        blank=True,
    )

    share_link = models.URLField(
        max_length=1024,
        help_text='Link that will be put in share button',
        blank=True,
        editable=False,
    )

    share_link_text = models.CharField(
        max_length=20,
        help_text='Text content of the share button',
        default='Share this',
        blank=True,
        editable=False,
    )

    share_twitter = models.CharField(
        max_length=20,
        help_text='Share Progress id for twitter button',
        blank=True,
    )

    share_facebook = models.CharField(
        max_length=20,
        help_text='Share Progress id for facebook button',
        blank=True,
    )

    share_email = models.CharField(
        max_length=20,
        help_text='Share Progress id for email button',
        blank=True,
    )

    thank_you = models.CharField(
        max_length=140,
        help_text='Message to show after thanking people for signing',
        default='Thank you for signing too!',
    )

    class Meta:
        verbose_name = 'petition snippet'
