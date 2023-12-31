# Generated by Django 4.2.3 on 2023-07-31 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=256)),
                ('short_link_id', models.CharField(editable=False, max_length=10, unique=True)),
            ],
        ),
    ]
