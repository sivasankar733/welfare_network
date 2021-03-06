# Generated by Django 3.0.4 on 2020-04-06 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('idno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('pas', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contactno', models.IntegerField(unique=True)),
                ('dob', models.DateField()),
                ('companyname', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CelebrationsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=200)),
                ('contactno', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='EventsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('description', models.CharField(max_length=100)),
                ('contactno', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='matrimonialModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brifegrom_name', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('description', models.CharField(max_length=100)),
                ('contactno', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('property_type', models.CharField(max_length=50)),
                ('property_title', models.CharField(max_length=100)),
                ('area_size', models.IntegerField()),
                ('price', models.FloatField()),
                ('address', models.CharField(max_length=100)),
                ('contactno', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReferencesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('job_title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=70)),
                ('lastdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationModel',
            fields=[
                ('idno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('pas', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('con', models.IntegerField(unique=True)),
                ('dob', models.DateField()),
                ('companynam', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='SharemarketModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('copmany_name', models.CharField(max_length=50)),
                ('share_value', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('technology', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('contactno', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TravelModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('travel_date', models.DateField()),
                ('location', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=100)),
                ('contactno', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserthoughtsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=100)),
                ('contact', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkexperienceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('technology', models.CharField(max_length=40)),
                ('workexperience', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
                ('contactno', models.IntegerField(unique=True)),
            ],
        ),
    ]
