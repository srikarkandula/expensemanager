# Generated by Django 3.1.4 on 2021-03-01 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210301_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.creator'),
        ),
    ]