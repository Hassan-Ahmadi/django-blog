# Generated by Django 3.2 on 2024-01-20 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='status',
            new_name='is_published',
        ),
    ]
