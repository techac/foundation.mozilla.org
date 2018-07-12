# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-12 22:34
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.blocks.static_block
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0031_auto_20180607_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modularpage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'h5', 'ol', 'ul', 'link', 'hr'])), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('captionURL', wagtail.core.blocks.CharBlock(help_text='Optional URL that this caption should link out to.', required=False))))), ('image_text', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'])), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True))))), ('ordering', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Image on the left'), ('right', 'Image on the right')]))))), ('image_text2', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['link', 'h2', 'h3', 'h4', 'h5', 'h6'])), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this image should link out to.', required=False)), ('small', wagtail.core.blocks.BooleanBlock(help_text='Use smaller, fixed image size (eg: icon)', required=False))))), ('figure', wagtail.core.blocks.StructBlock((('figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Do not apply any explicit alignment classes.'), ('left-align', 'Left-align this image with the page content.'), ('right-align', 'Right-align this image with the page content.'), ('center', 'Center this image with the page content.'), ('full-width', 'Make this image full-width.')], required=False))))), ('caption', wagtail.core.blocks.CharBlock(help_text='Please remember to properly attribute any images we use.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this figure should link out to.', required=False))))), ('figuregrid', wagtail.core.blocks.StructBlock((('grid_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Do not apply any explicit alignment classes.'), ('left-align', 'Left-align this image with the page content.'), ('right-align', 'Right-align this image with the page content.'), ('center', 'Center this image with the page content.'), ('full-width', 'Make this image full-width.')], required=False))))), ('caption', wagtail.core.blocks.CharBlock(help_text='Please remember to properly attribute any images we use.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this figure should link out to.', required=False)))))),))), ('figuregrid2', wagtail.core.blocks.StructBlock((('grid_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(help_text='Please remember to properly attribute any images we use.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this figure should link out to.', required=False)))))),))), ('video', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.CharBlock(help_text='Please make sure this is a proper embed URL, or your video will not show up on the page.')), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('captionURL', wagtail.core.blocks.CharBlock(help_text='Optional URL for caption to link to.', required=False))))), ('iframe', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.CharBlock(help_text='Please note that only URLs from white-listed domains will work.')), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('captionURL', wagtail.core.blocks.CharBlock(help_text='Optional URL that this caption should link out to.', required=False))))), ('linkbutton', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('URL', wagtail.core.blocks.CharBlock()), ('styling', wagtail.core.blocks.ChoiceBlock(choices=[('btn-normal', 'Normal button'), ('btn-ghost', 'Ghost button')]))))), ('spacer', wagtail.core.blocks.StructBlock((('size', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'quarter spacing'), ('2', 'half spacing'), ('3', 'single spacing'), ('4', 'one and a half spacing'), ('5', 'triple spacing')])),))), ('quote', wagtail.core.blocks.StructBlock((('quotes', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.CharBlock()), ('attribution', wagtail.core.blocks.CharBlock()))))),))), ('pulse_listing', wagtail.core.blocks.StructBlock((('search_terms', wagtail.core.blocks.CharBlock(help_text='Test your search at mozillapulse.org/search', label='Search', required=False)), ('max_number_of_results', wagtail.core.blocks.IntegerBlock(default=6, help_text='Choose 1-12. If you want visitors to see more, link to a search or tag on Pulse.', max_value=12, min_value=0, required=True)), ('only_featured_entries', wagtail.core.blocks.BooleanBlock(default=False, help_text='Featured items are selected by Pulse moderators.', label='Display only featured entries', required=False)), ('newest_first', wagtail.core.blocks.ChoiceBlock(choices=[('True', 'Show newer entries first'), ('False', 'Show older entries first')], label='Sort')), ('advanced_filter_header', wagtail.core.blocks.static_block.StaticBlock(admin_text='-------- ADVANCED FILTERS: OPTIONS TO DISPLAY FEWER, MORE TARGETED RESULTS. --------', label=' ')), ('issues', wagtail.core.blocks.ChoiceBlock(choices=[('all', 'All'), ('Decentralization', 'Decentralization'), ('Digital Inclusion', 'Digital Inclusion'), ('Online Privacy & Security', 'Online Privacy & Security'), ('Open Innovation', 'Open Innovation'), ('Web Literacy', 'Web Literacy')])), ('help', wagtail.core.blocks.ChoiceBlock(choices=[('all', 'All'), ('Attend', 'Attend'), ('Create content', 'Create content'), ('Code', 'Code'), ('Design', 'Design'), ('Fundraise', 'Fundraise'), ('Join community', 'Join community'), ('Localize & translate', 'Localize & translate'), ('Mentor', 'Mentor'), ('Plan & organize', 'Plan & organize'), ('Promote', 'Promote'), ('Take action', 'Take action'), ('Test & feedback', 'Test & feedback'), ('Write documentation', 'Write documentation')], label='Type of help needed'))))))),
        ),
        migrations.AlterField(
            model_name='primarypage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'h5', 'ol', 'ul', 'link', 'hr'])), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('captionURL', wagtail.core.blocks.CharBlock(help_text='Optional URL that this caption should link out to.', required=False))))), ('image_text', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'])), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True))))), ('ordering', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Image on the left'), ('right', 'Image on the right')]))))), ('image_text2', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['link', 'h2', 'h3', 'h4', 'h5', 'h6'])), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this image should link out to.', required=False)), ('small', wagtail.core.blocks.BooleanBlock(help_text='Use smaller, fixed image size (eg: icon)', required=False))))), ('figure', wagtail.core.blocks.StructBlock((('figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Do not apply any explicit alignment classes.'), ('left-align', 'Left-align this image with the page content.'), ('right-align', 'Right-align this image with the page content.'), ('center', 'Center this image with the page content.'), ('full-width', 'Make this image full-width.')], required=False))))), ('caption', wagtail.core.blocks.CharBlock(help_text='Please remember to properly attribute any images we use.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this figure should link out to.', required=False))))), ('figuregrid', wagtail.core.blocks.StructBlock((('grid_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Do not apply any explicit alignment classes.'), ('left-align', 'Left-align this image with the page content.'), ('right-align', 'Right-align this image with the page content.'), ('center', 'Center this image with the page content.'), ('full-width', 'Make this image full-width.')], required=False))))), ('caption', wagtail.core.blocks.CharBlock(help_text='Please remember to properly attribute any images we use.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this figure should link out to.', required=False)))))),))), ('figuregrid2', wagtail.core.blocks.StructBlock((('grid_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(help_text='Please remember to properly attribute any images we use.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this figure should link out to.', required=False)))))),))), ('video', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.CharBlock(help_text='Please make sure this is a proper embed URL, or your video will not show up on the page.')), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('captionURL', wagtail.core.blocks.CharBlock(help_text='Optional URL for caption to link to.', required=False))))), ('iframe', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.CharBlock(help_text='Please note that only URLs from white-listed domains will work.')), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('captionURL', wagtail.core.blocks.CharBlock(help_text='Optional URL that this caption should link out to.', required=False))))), ('linkbutton', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('URL', wagtail.core.blocks.CharBlock()), ('styling', wagtail.core.blocks.ChoiceBlock(choices=[('btn-normal', 'Normal button'), ('btn-ghost', 'Ghost button')]))))), ('spacer', wagtail.core.blocks.StructBlock((('size', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'quarter spacing'), ('2', 'half spacing'), ('3', 'single spacing'), ('4', 'one and a half spacing'), ('5', 'triple spacing')])),))), ('quote', wagtail.core.blocks.StructBlock((('quotes', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.CharBlock()), ('attribution', wagtail.core.blocks.CharBlock()))))),))), ('pulse_listing', wagtail.core.blocks.StructBlock((('search_terms', wagtail.core.blocks.CharBlock(help_text='Test your search at mozillapulse.org/search', label='Search', required=False)), ('max_number_of_results', wagtail.core.blocks.IntegerBlock(default=6, help_text='Choose 1-12. If you want visitors to see more, link to a search or tag on Pulse.', max_value=12, min_value=0, required=True)), ('only_featured_entries', wagtail.core.blocks.BooleanBlock(default=False, help_text='Featured items are selected by Pulse moderators.', label='Display only featured entries', required=False)), ('newest_first', wagtail.core.blocks.ChoiceBlock(choices=[('True', 'Show newer entries first'), ('False', 'Show older entries first')], label='Sort')), ('advanced_filter_header', wagtail.core.blocks.static_block.StaticBlock(admin_text='-------- ADVANCED FILTERS: OPTIONS TO DISPLAY FEWER, MORE TARGETED RESULTS. --------', label=' ')), ('issues', wagtail.core.blocks.ChoiceBlock(choices=[('all', 'All'), ('Decentralization', 'Decentralization'), ('Digital Inclusion', 'Digital Inclusion'), ('Online Privacy & Security', 'Online Privacy & Security'), ('Open Innovation', 'Open Innovation'), ('Web Literacy', 'Web Literacy')])), ('help', wagtail.core.blocks.ChoiceBlock(choices=[('all', 'All'), ('Attend', 'Attend'), ('Create content', 'Create content'), ('Code', 'Code'), ('Design', 'Design'), ('Fundraise', 'Fundraise'), ('Join community', 'Join community'), ('Localize & translate', 'Localize & translate'), ('Mentor', 'Mentor'), ('Plan & organize', 'Plan & organize'), ('Promote', 'Promote'), ('Take action', 'Take action'), ('Test & feedback', 'Test & feedback'), ('Write documentation', 'Write documentation')], label='Type of help needed'))))))),
        ),
    ]
