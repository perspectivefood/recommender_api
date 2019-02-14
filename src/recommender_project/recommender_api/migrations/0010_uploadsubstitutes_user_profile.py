# Generated by Django 2.1.5 on 2019-02-14 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommender_api', '0009_uploadsubstitutes'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadsubstitutes',
            name='user_profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
