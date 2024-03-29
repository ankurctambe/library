# Generated by Django 5.0 on 2024-01-15 06:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(blank=True, max_length=20, null=True)),
                ('quantity', models.CharField(blank=True, max_length=10, null=True)),
                ('buyer', models.CharField(blank=True, max_length=10, null=True)),
                ('dt', models.DateField(blank=True, max_length=10, null=True)),
                ('dr', models.DateField(blank=True, max_length=10, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='library1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
