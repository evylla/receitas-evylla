# Generated by Django 3.2.6 on 2021-08-09 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20201130_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
