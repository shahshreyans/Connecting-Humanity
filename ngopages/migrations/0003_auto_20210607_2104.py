# Generated by Django 3.2.3 on 2021-06-07 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngopages', '0002_auto_20210603_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerngomodel',
            name='mission',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='registerngomodel',
            name='ngo_logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
