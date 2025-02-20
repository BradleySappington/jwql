# Generated by Django 4.1.7 on 2024-03-20 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwql', '0019_alter_fgsreadnoisequeryhistory_aperture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='category',
            field=models.CharField(default='empty', help_text='Category Type', max_length=10),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='thumbnail_path',
            field=models.CharField(default='empty', help_text='Path to the proposal thumbnail', max_length=1000),
        ),
        migrations.AlterField(
            model_name='rootfileinfo',
            name='aperture',
            field=models.CharField(blank=True, default='empty', help_text='Aperture', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='rootfileinfo',
            name='detector',
            field=models.CharField(blank=True, default='empty', help_text='Detector', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='rootfileinfo',
            name='exp_type',
            field=models.CharField(blank=True, default='empty', help_text='Exposure Type', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='rootfileinfo',
            name='filter',
            field=models.CharField(blank=True, default='empty', help_text='Instrument name', max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='rootfileinfo',
            name='grating',
            field=models.CharField(blank=True, default='empty', help_text='Grating', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='rootfileinfo',
            name='pupil',
            field=models.CharField(blank=True, default='empty', help_text='Pupil', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='rootfileinfo',
            name='read_patt',
            field=models.CharField(blank=True, default='empty', help_text='Read Pattern', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='rootfileinfo',
            name='subarray',
            field=models.CharField(blank=True, default='empty', help_text='Subarray', max_length=40, null=True),
        ),
    ]
