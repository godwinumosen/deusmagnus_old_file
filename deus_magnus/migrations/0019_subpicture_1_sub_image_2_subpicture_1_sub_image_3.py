# Generated by Django 5.1.4 on 2025-01-22 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deus_magnus', '0018_delete_teammemberbirthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='subpicture_1',
            name='sub_image_2',
            field=models.ImageField(default=1, upload_to='images_sub2/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subpicture_1',
            name='sub_image_3',
            field=models.ImageField(default=1, upload_to='images_sub2/'),
            preserve_default=False,
        ),
    ]
