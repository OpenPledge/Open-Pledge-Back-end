# Generated by Django 2.0.8 on 2018-10-05 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0004_pledge_pledged_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='pledged_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]