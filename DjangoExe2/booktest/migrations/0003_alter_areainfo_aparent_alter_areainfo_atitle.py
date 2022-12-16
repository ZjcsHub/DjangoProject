# Generated by Django 4.1.3 on 2022-12-12 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_areainfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areainfo',
            name='aParent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='booktest.areainfo', verbose_name='父级地区'),
        ),
        migrations.AlterField(
            model_name='areainfo',
            name='atitle',
            field=models.CharField(max_length=20, verbose_name='标题'),
        ),
    ]
