# Generated by Django 2.1.5 on 2019-02-12 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender_api', '0002_auto_20190212_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedmenueplan',
            name='PLU',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
