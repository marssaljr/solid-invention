# Generated by Django 4.0.2 on 2022-02-08 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tag',
            new_name='Category',
        ),
        migrations.RemoveField(
            model_name='project',
            name='tags',
        ),
        migrations.AddField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(related_name='categories', to='projects.Category'),
        ),
    ]
