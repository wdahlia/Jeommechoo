# Generated by Django 3.2.13 on 2022-11-02 10:57

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/review_file'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/review_file'),
        ),
    ]
