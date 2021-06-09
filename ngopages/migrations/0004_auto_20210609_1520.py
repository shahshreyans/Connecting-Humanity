# Generated by Django 3.2.3 on 2021-06-09 09:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngopages', '0003_auto_20210607_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerngomodel',
            name='contact_number',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Contact No. Format:'+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='registerngomodel',
            name='ngo_logo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]