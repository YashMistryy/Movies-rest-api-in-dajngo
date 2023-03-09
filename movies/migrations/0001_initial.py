# Generated by Django 4.1.7 on 2023-03-09 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=100)),
                ('movie_releaseDate', models.DateField()),
                ('movie_rating', models.IntegerField(max_length=1)),
            ],
        ),
    ]