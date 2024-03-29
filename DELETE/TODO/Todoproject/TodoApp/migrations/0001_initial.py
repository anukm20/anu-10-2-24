# Generated by Django 4.2.9 on 2024-01-10 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=25)),
                ('priority', models.IntegerField()),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='todoimage')),
            ],
        ),
    ]
