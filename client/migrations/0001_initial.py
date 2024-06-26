# Generated by Django 5.0.6 on 2024-05-15 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('date_of_birth', models.CharField(max_length=8)),
                ('expiration_date', models.CharField(max_length=8)),
                ('gender', models.CharField(max_length=1)),
                ('personal_number', models.CharField(max_length=14, unique=True)),
                ('card_number', models.CharField(max_length=9, unique=True)),
                ('nationality', models.CharField(max_length=8)),
            ],
        ),
    ]
