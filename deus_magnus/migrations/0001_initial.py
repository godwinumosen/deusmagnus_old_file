# Generated by Django 5.0.1 on 2024-04-17 08:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeusMagnusMainPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deus_magnus_title', models.CharField(blank=True, max_length=255, null=True)),
                ('deus_magnus_description', models.TextField()),
                ('deus_magnus_slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('deus_magnus_img', models.ImageField(upload_to='image/')),
                ('deus_magnus_publish_date', models.DateTimeField(auto_now_add=True)),
                ('deus_magnus_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-deus_magnus_publish_date'],
            },
        ),
    ]
