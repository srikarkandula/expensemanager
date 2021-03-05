# Generated by Django 3.1.4 on 2021-02-26 16:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210226_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.FloatField()),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('reason', models.CharField(blank=True, choices=[('Home', 'Home'), ('Construction', 'Construction'), ('Medical', 'Medical'), ('Education', 'Education'), ('Electronics', 'Electronics'), ('Services', 'Services'), ('Gifts', 'Gifts'), ('Travel', 'Travel'), ('Kids', 'Kids'), ('Pet', 'Pet'), ('Others', 'Others')], max_length=1000, null=True)),
                ('important', models.BooleanField(default=False)),
                ('month', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
