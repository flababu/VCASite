# Generated by Django 2.2.5 on 2019-11-14 07:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='YearLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_level', models.CharField(max_length=100)),
                ('school_level', models.CharField(choices=[('Preschool', 'Preschool'), ('Gradeschool', 'Gradeschool'), ('JuniorHighschool', 'Junior Highschool'), ('SeniorHighschool', 'Senior Highschool'), ('Unspecified', 'None')], default='None', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('middle_name', models.CharField(max_length=100, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('student_number', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999999999)])),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Parent')),
                ('section', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Information.Section')),
                ('year_level', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Information.YearLevel')),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='year_level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Information.YearLevel'),
        ),
    ]