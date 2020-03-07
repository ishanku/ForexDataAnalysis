# Generated by Django 3.0.4 on 2020-03-07 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForexCurrent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('AUD', models.DecimalField(decimal_places=2, max_digits=23)),
                ('EUR', models.DecimalField(decimal_places=2, max_digits=23)),
                ('NCD', models.DecimalField(decimal_places=2, max_digits=23)),
                ('GBP', models.DecimalField(decimal_places=2, max_digits=23)),
                ('BRL', models.DecimalField(decimal_places=2, max_digits=23)),
                ('CAD', models.DecimalField(decimal_places=2, max_digits=23)),
                ('CNY', models.DecimalField(decimal_places=2, max_digits=23)),
                ('HKD', models.DecimalField(decimal_places=2, max_digits=23)),
                ('INR', models.DecimalField(decimal_places=2, max_digits=23)),
                ('KRW', models.DecimalField(decimal_places=2, max_digits=23)),
                ('MXN', models.DecimalField(decimal_places=2, max_digits=23)),
                ('ZAR', models.DecimalField(decimal_places=2, max_digits=23)),
                ('SGD', models.DecimalField(decimal_places=2, max_digits=23)),
                ('DKK', models.DecimalField(decimal_places=2, max_digits=23)),
                ('JPY', models.DecimalField(decimal_places=2, max_digits=23)),
                ('MYR', models.DecimalField(decimal_places=2, max_digits=23)),
                ('NOK', models.DecimalField(decimal_places=2, max_digits=23)),
                ('SEK', models.DecimalField(decimal_places=2, max_digits=23)),
                ('LKR', models.DecimalField(decimal_places=2, max_digits=23)),
                ('CHF', models.DecimalField(decimal_places=2, max_digits=23)),
                ('TWD', models.DecimalField(decimal_places=2, max_digits=23)),
                ('THB', models.DecimalField(decimal_places=2, max_digits=23)),
            ],
            options={
                'verbose_name_plural': 'ForexCurrentRates',
                'db_table': 'ForexCurrent',
            },
        ),
    ]
