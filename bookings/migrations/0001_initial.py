# Generated by Django 5.1.5 on 2025-02-06 01:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trips', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    # operations = [
    #     migrations.CreateModel(
    #         name='Booking',
    #         fields=[
    #             ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
    #             ('seats', models.PositiveIntegerField()),
    #             ('booked_at', models.DateTimeField(auto_now_add=True)),
    #             ('status', models.CharField(default='pending', max_length=20)),
    #             ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.trip')),
    #             ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
    #         ],
    #     ),
    # ]
