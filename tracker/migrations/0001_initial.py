# Generated by Django 3.0.4 on 2020-03-17 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SuspectedCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.SmallIntegerField()),
                ('age', models.SmallIntegerField()),
                ('symptoms_date', models.DateField()),
                ('origin_country', models.CharField(max_length=30)),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.State')),
            ],
        ),
        migrations.CreateModel(
            name='ConfirmedCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.SmallIntegerField()),
                ('age', models.SmallIntegerField()),
                ('symptoms_date', models.DateField()),
                ('origin_country', models.CharField(max_length=30)),
                ('healed', models.BooleanField()),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.State')),
            ],
        ),
    ]
