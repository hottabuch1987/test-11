# Generated by Django 4.2.16 on 2024-11-11 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderimage',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]