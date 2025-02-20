# Generated by Django 5.0.3 on 2024-04-02 23:17

import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=320)),
                ('phone_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddConstraint(
            model_name='member',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('email'), name='unique_email'),
        ),
        migrations.AddConstraint(
            model_name='member',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('phone_number'), name='unique_phone_number'),
        ),
    ]
