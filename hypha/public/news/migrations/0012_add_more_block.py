# Generated by Django 2.2.19 on 2021-02-28 21:34

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_add_box_apply_link_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title', icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('box', wagtail.core.blocks.StructBlock([('box_content', wagtail.core.blocks.RichTextBlock()), ('box_class', wagtail.core.blocks.CharBlock(required=False))])), ('more', wagtail.core.blocks.StructBlock([('more_content', wagtail.core.blocks.RichTextBlock()), ('more_content_more', wagtail.core.blocks.RichTextBlock()), ('more_class', wagtail.core.blocks.CharBlock(required=False))])), ('apply_link', wagtail.core.blocks.StructBlock([('application', wagtail.core.blocks.PageChooserBlock())])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.CharBlock(form_classname='title')), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('job_title', wagtail.core.blocks.CharBlock(required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('call_to_action', wagtail.snippets.blocks.SnippetChooserBlock('utils.CallToActionSnippet', template='blocks/call_to_action_block.html')), ('document', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock()), ('title', wagtail.core.blocks.CharBlock(required=False))])), ('awesome_table_widget', wagtail.core.blocks.StructBlock([('table_id', wagtail.core.blocks.CharBlock(form_classname='title', help_text='Please enter only table id from embed code. Table widget code creates automatically.'))]))]),
        ),
    ]
