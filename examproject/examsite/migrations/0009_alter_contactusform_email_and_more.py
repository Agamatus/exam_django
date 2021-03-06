# Generated by Django 4.0.3 on 2022-04-01 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examsite', '0008_alter_portfolio_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactusform',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name="User's Email"),
        ),
        migrations.AlterField(
            model_name='contactusform',
            name='message',
            field=models.TextField(max_length=300, verbose_name="User's Message"),
        ),
        migrations.AlterField(
            model_name='contactusform',
            name='name',
            field=models.CharField(max_length=32, verbose_name="User's Name"),
        ),
    ]
