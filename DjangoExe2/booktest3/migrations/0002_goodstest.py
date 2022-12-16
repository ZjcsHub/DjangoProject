# Generated by Django 4.1.3 on 2022-12-14 08:55

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(0, '下架'), (1, '上架')], verbose_name='商品状态')),
                ('detail', tinymce.models.HTMLField()),
            ],
        ),
    ]