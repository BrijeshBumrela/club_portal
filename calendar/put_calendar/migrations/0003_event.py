# Generated by Django 2.1.3 on 2019-01-06 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('put_calendar', '0002_check_date_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=256)),
                ('event_date', models.DateField()),
            ],
        ),
    ]
