# Generated by Django 3.0.5 on 2020-05-02 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('shortname', models.CharField(max_length=10)),
                ('postcode', models.CharField(max_length=10)),
                ('code', models.CharField(max_length=10)),
                ('location_type', models.CharField(choices=[('Continent', 'Continent'), ('Country', 'Country'), ('State', 'State'), ('Departament', 'Departament'), ('Municipality', 'Municipality'), ('City', 'City'), ('Town', 'Town'), ('Zone', 'Zone')], editable=False, max_length=50)),
                ('latitude', models.FloatField(max_length=20, null=True)),
                ('longitude', models.FloatField(max_length=20, null=True)),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.Language')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.Location')),
            ],
        ),
    ]
