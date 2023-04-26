# Generated by Django 4.0.3 on 2023-04-26 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=30)),
                ('price', models.DecimalField(decimal_places=1, default='', max_digits=20)),
            ],
        ),
    ]
