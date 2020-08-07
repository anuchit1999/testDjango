# Generated by Django 2.0 on 2020-02-07 17:23

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=60)),
                ('quote', models.CharField(max_length=200)),
                ('client_pic', models.ImageField(upload_to='client/')),
                ('pic_avata', models.ImageField(upload_to='avatar/')),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]