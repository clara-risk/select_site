# Generated by Django 4.0.4 on 2022-05-18 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitemap', '0007_asm_geom'),
    ]

    operations = [
        migrations.CreateModel(
            name='EXPORT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etype', models.CharField(default='GeoJSON', max_length=50)),
            ],
        ),
    ]
