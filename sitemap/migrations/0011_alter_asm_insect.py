# Generated by Django 4.0.4 on 2022-05-27 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitemap', '0010_force_filter_droad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asm',
            name='insect',
            field=models.CharField(choices=[('Jack Pine Budworm', 'Jack Pine Budworm'), ('Spruce Budworm', 'Spruce Budworm')], default='Jack Pine Budworm', max_length=50),
        ),
    ]
