# Generated by Django 5.1.6 on 2025-02-07 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('description', models.TextField(default='No description')),
                ('image', models.ImageField(upload_to='team/')),
                ('phone', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
