# Generated by Django 3.2.8 on 2021-10-16 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('low', models.DecimalField(decimal_places=5, max_digits=10)),
                ('high', models.DecimalField(decimal_places=5, max_digits=10)),
                ('open', models.DecimalField(decimal_places=5, max_digits=10)),
                ('close', models.DecimalField(decimal_places=5, max_digits=10)),
                ('ticker_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tickers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
    ]
