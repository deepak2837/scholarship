# Generated by Django 2.2.7 on 2020-07-26 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_auto_20200714_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='both',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='boy',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='girl',
            field=models.IntegerField(blank=True, default=-1, null=True),
        ),
    ]
