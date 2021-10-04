# Generated by Django 3.2.7 on 2021-10-04 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_calculator', '0004_alter_user_smoker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.CharField(choices=[('southwest', 0), ('southeast', 1), ('northwest', 2), ('northeast', 3)], default='southeast', max_length=50),
        ),
    ]
