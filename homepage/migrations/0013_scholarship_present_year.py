# Generated by Django 2.2.7 on 2020-07-31 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_session_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='present_year',
            field=models.CharField(blank=True, default='FE', max_length=30, null=True),
        ),
    ]
