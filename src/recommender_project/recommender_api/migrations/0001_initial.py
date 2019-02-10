# Generated by Django 2.1.5 on 2019-02-09 16:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProfileFeedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startup_name', models.CharField(blank=True, max_length=255, null=True)),
                ('management_experience', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(0)])),
                ('technical_experience', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(0)])),
                ('startup_experience', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(0)])),
                ('founders', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('advisors', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('employees', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(0)])),
                ('budget', models.CharField(blank=True, choices=[('verysmall', '<10k'), ('small', '10k-50k'), ('medium', '50k-100k'), ('big', '100k-500k'), ('verybig', '>500k')], default='verysmall', max_length=10, null=True)),
                ('funding_rounds', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('focus', models.CharField(blank=True, choices=[('B2B', 'B2B'), ('B2C', 'B2C')], default='B2C', max_length=10, null=True)),
                ('founding_date', models.DateField(blank=True, default='1900-01-01', null=True)),
                ('revenue', models.IntegerField(blank=True, null=True)),
                ('hightech', models.CharField(blank=True, choices=[(1, 'YES'), (0, 'NO')], max_length=255, null=True)),
                ('industry', models.CharField(blank=True, choices=[('MedHealthTech', 'MedHealthTech'), ('ICT App', 'ICT App'), ('AgriFoodTech', 'AgriFoodTech'), ('FinInsureTech', 'FinInsureTech'), ('HighTech', 'HighTech'), ('AdRetailTech', 'AdRetailTech'), ('CleanGreenTech', 'CleanGreenTech'), ('Consumer Goods', 'Consumer Goods'), ('PropTech', 'PropTech'), ('Consumer Goods', 'Consumer Goods'), ('RegLegalTech', 'RegLegalTech'), ('BioTech', 'BioTech'), ('MobilityTravelTech', 'MobilityTravelTech'), ('Other', 'Other')], max_length=255, null=True)),
                ('hotspot', models.CharField(blank=True, choices=[(1, 'YES'), (0, 'NO')], max_length=255, null=True)),
                ('status', models.CharField(blank=True, choices=[('living', 'living'), ('survived', 'survived'), ('dead', 'dead')], default='living', max_length=255, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]