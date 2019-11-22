# Generated by Django 2.2.7 on 2019-11-22 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogNo', models.IntegerField()),
                ('title', models.TextField(max_length=50)),
                ('publicationDate', models.DateTimeField()),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
