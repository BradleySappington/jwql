# Generated by Django 4.1.7 on 2024-04-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwql', '0020_alter_proposal_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rootfileinfo',
            name='read_patt_num',
            field=models.IntegerField(default=1, help_text='Read Pattern Number'),
        ),
    ]
