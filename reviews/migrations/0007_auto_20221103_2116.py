# Generated by Django 3.2.13 on 2022-11-03 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0011_alter_restaurant_table'),
        ('reviews', '0006_alter_review_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant', to='restaurants.restaurant'),
        ),
        migrations.AlterModelTable(
            name='review',
            table=None,
        ),
    ]