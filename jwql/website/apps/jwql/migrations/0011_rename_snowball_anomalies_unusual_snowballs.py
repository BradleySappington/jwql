# Generated by Django 4.1.7 on 2024-01-12 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jwql', '0010_auto_20230313_1053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anomalies',
            old_name='snowball',
            new_name='unusual_snowballs',
        ),
    ]
