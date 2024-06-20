# Generated by Django 4.2.13 on 2024-06-19 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date', models.DateField()),
            ],
        ),
    ]