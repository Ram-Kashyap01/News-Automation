# Generated by Django 3.1.7 on 2021-05-22 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_auto_20210522_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prefer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sports', models.CharField(default='not', max_length=20)),
                ('politics', models.CharField(default='not', max_length=20)),
                ('education', models.CharField(default='not', max_length=20)),
                ('business', models.CharField(default='not', max_length=20)),
                ('films', models.CharField(default='not', max_length=20)),
                ('email', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
