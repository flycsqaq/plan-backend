# Generated by Django 2.2 on 2019-04-23 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('time', models.DateField()),
                ('isCompleted', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=400)),
            ],
        ),
    ]
