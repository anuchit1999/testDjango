# Generated by Django 2.0 on 2020-02-04 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=80)),
                ('course_date', models.DateField(auto_now_add=True)),
                ('course_info', models.TextField()),
                ('skill_required', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('course_photo', models.ImageField(upload_to='course/')),
                ('course_duration', models.CharField(max_length=40)),
            ],
        ),
    ]
