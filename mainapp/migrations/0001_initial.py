# Generated by Django 4.2.6 on 2023-11-14 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SMS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_number', models.CharField(max_length=15)),
                ('message', models.TextField()),
            ],
        ),
    ]
