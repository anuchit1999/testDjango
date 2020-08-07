# Generated by Django 2.0 on 2020-08-07 09:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200208_0023'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_description', models.TextField()),
                ('main_header_cover', models.ImageField(upload_to='main_cover/')),
                ('sub_header_cover', models.ImageField(upload_to='sub_cover/')),
                ('box_name1', models.CharField(max_length=20)),
                ('box_name2', models.CharField(max_length=20)),
                ('box_name_small', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='course_date',
            field=models.DateField(),
        ),
    ]