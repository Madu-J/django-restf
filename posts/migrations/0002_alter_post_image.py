# Generated by Django 3.2.25 on 2024-03-22 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_dwzcuabfl', upload_to='images/'),
        ),
    ]
