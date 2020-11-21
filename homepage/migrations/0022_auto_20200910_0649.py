# Generated by Django 2.2.7 on 2020-09-10 01:19

from django.db import migrations, models
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0021_auto_20200908_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='document',
            field=models.FileField(upload_to='documents/scholarship_broucher/', validators=[homepage.models.file_size]),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='scholarship_form',
            field=models.FileField(default='documents/scholarship_form/default_scholarship_form.pdf', upload_to='documents/scholarship_form/', validators=[homepage.models.file_size]),
        ),
    ]
