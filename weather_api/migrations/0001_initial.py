# Generated by Django 3.2.7 on 2021-09-16 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coord', models.JSONField(db_column='coord')),
                ('weather', models.JSONField(db_column='weather')),
                ('base', models.CharField(db_column='base', max_length=200)),
                ('main', models.JSONField(db_column='main')),
                ('visibility', models.IntegerField(db_column='visibility')),
                ('wind', models.JSONField(db_column='wind')),
                ('clouds', models.JSONField(db_column='clouds')),
                ('dt', models.IntegerField(db_column='dt')),
                ('sys', models.JSONField(db_column='sys')),
                ('timezone', models.IntegerField(db_column='timezone')),
                ('id_city', models.IntegerField(db_column='id_city')),
                ('name', models.CharField(db_column='name', max_length=200)),
                ('cod', models.IntegerField(db_column='cod')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at')),
            ],
            options={
                'db_table': 'city',
                'managed': True,
            },
        ),
    ]