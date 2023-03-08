# Generated by Django 3.2.18 on 2023-03-07 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network', models.CharField(max_length=100)),
                ('link', models.URLField(max_length=100)),
                ('image', models.FilePathField(path='/img')),
            ],
        ),
    ]
