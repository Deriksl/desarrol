# Generated by Django 5.1.1 on 2024-09-19 00:59

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
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='titulo')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('datecompleted', models.DateTimeField(default='', null=True, verbose_name='fecha completado')),
                ('important', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
