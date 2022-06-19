# Generated by Django 4.0.5 on 2022-06-19 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneBookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('mobile', models.CharField(max_length=225)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/user')),
            ],
        ),
    ]
