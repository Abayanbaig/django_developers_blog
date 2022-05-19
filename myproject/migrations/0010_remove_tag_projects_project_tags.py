# Generated by Django 4.0.1 on 2022-01-20 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0009_remove_project_tags_tag_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='projects',
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, to='myproject.Tag'),
        ),
    ]
