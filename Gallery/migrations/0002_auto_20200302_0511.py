# Generated by Django 3.0.3 on 2020-03-02 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
