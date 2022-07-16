# Generated by Django 2.2.6 on 2019-12-30 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('applicants', models.IntegerField()),
                ('short_description', models.CharField(max_length=50)),
                ('long_description', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
                ('boy', models.BooleanField(default=False)),
                ('girl', models.BooleanField(default=False)),
                ('both', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('document', models.FileField(upload_to='documents/')),
                ('fromdate', models.DateField(null=True)),
                ('toomdate', models.DateField(null=True)),
            ],
        ),
    ]