# Generated by Django 2.2.3 on 2019-07-03 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dobby', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='rent_month',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='rent_year',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]