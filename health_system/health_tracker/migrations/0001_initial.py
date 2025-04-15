# Generated by Django 5.0.7 on 2025-04-15 10:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeightRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('note', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
