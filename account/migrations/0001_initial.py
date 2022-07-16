# Generated by Django 3.0.5 on 2020-11-20 19:25

import account.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_no', models.IntegerField(validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(20000)])),
                ('name', models.CharField(max_length=20)),
                ('branch', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('email', models.EmailField(max_length=250)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.IntegerField(validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(20000)])),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=250)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.IntegerField(default=0)),
                ('division', models.IntegerField(default=0)),
                ('mobile', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(default='', max_length=20)),
                ('marks', models.IntegerField(blank=True, default=0, null=True)),
                ('father_rank', models.CharField(choices=[('Lance Naik', 'Lance Naik'), ('Naik', 'Naik'), ('Hawaldar', 'Hawaldar'), ('Nb Subedar', 'Nb Subedar'), ('Subedar', 'Subedar'), ('Subeder Maj', 'Subeder Maj'), ('Officer', 'Officer')], default='Officer', max_length=50)),
                ('father_name', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('present_year', models.CharField(choices=[('FE', 'FE'), ('SE', 'SE'), ('TE', 'TE'), ('BE', 'BE')], default='FE', max_length=30)),
                ('attendence', models.IntegerField(blank=True, default=0, null=True)),
                ('image', models.ImageField(default='pics/profile_pics/default.png', upload_to='pics/profile_pics', validators=[account.models.file_size])),
                ('roll_no', models.IntegerField(default=0)),
                ('address', models.CharField(default='', max_length=50)),
                ('document10', models.FileField(blank=True, null=True, upload_to='documents/user_documents/10marksheets', validators=[account.models.file_size])),
                ('document12', models.FileField(blank=True, null=True, upload_to='documents/user_documents/12marksheets', validators=[account.models.file_size])),
                ('document_last_sem', models.FileField(blank=True, null=True, upload_to='documents/user_documents/last_marksheets', validators=[account.models.file_size])),
                ('father_id', models.FileField(blank=True, null=True, upload_to='documents/user_documents/father_id', validators=[account.models.file_size])),
                ('student_id', models.FileField(blank=True, null=True, upload_to='documents/user_documents/student_id', validators=[account.models.file_size])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]