# Generated by Django 3.1.14 on 2021-12-21 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0011_auto_20211217_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45)),
                ('unit', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Performances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performance', models.SmallIntegerField(blank=True, null=True)),
                ('performedat', models.DateField(blank=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', null=True)),
                ('discipline_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.discipline')),
            ],
            options={
                'ordering': ['performedat'],
            },
        ),
    ]
