# Generated by Django 4.1.3 on 2022-12-12 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pictest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_pic', models.ImageField(upload_to='booktest3')),
            ],
        ),
    ]
