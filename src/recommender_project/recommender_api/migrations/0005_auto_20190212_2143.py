# Generated by Django 2.1.5 on 2019-02-12 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommender_api', '0004_page'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='user',
            new_name='user_profile',
        ),
    ]