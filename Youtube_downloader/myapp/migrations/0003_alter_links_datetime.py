# Generated by Django 4.2.5 on 2023-09-08 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_links_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
