# Generated by Django 4.1.2 on 2022-11-01 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_new_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_user',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='new_user',
            name='pass1',
            field=models.CharField(max_length=100, null=True),
        ),
    ]