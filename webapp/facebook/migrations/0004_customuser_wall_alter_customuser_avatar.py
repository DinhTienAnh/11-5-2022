# Generated by Django 4.0.4 on 2022-05-25 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0003_alter_customuser_avatar_alter_customuser_phonenumber_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='wall',
            field=models.ImageField(default=None, upload_to='facebook/images/user/wall/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(default=None, upload_to='facebook/images/user/avatar/%Y/%m'),
        ),
    ]
