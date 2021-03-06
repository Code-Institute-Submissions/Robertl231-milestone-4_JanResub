# Generated by Django 3.2 on 2022-01-10 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='defTruecountry',
            new_name='default_country',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='defTruecounty',
            new_name='default_county',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='defTruephone_number',
            new_name='default_phone_number',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='defTruepostcode',
            new_name='default_postcode',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='defTruestreet_address1',
            new_name='default_street_address1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='defTruestreet_address2',
            new_name='default_street_address2',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='defTruetown_or_city',
            new_name='default_town_or_city',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='defTrueuser',
            new_name='user',
        ),
    ]
