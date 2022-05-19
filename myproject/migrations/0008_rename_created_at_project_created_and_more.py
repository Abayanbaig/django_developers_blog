# Generated by Django 4.0.1 on 2022-01-19 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0007_tag_project_vote_ratio_alter_project_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RemoveField(
            model_name='project',
            name='language',
        ),
        migrations.AddField(
            model_name='project',
            name='demo_link',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='source_link',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]