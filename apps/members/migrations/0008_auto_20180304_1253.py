# Generated by Django 2.0.2 on 2018-03-04 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic'),
        ),
    ]