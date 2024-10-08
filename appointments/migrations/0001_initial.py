# Generated by Django 4.2.4 on 2023-09-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor','0001_initial')
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('contact', models.CharField(default='', max_length=10)),
                ('age', models.CharField(default='', max_length=2)),
                ('date', models.DateField(default='', max_length=10)),
                ('preference', models.BigIntegerField(default='',choices=(("1","A"),("2","B"),("3","C"),))),
                ('doctor_id', models.ForeignKey(default='',on_delete=models.SET_NULL, null=True, to='doctor.Doctor')),
            ],
            options={
                'db_table': 'appointments',
            },
        ),
    ]
