# Generated by Django 2.1.2 on 2018-10-26 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minstandard', models.CharField(default=1, max_length=30)),
                ('maxstandard', models.CharField(default=1, max_length=30)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaID', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=60)),
                ('father', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityID', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=50)),
                ('father', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='focus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='hotcity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityname', models.CharField(max_length=50, null=True)),
                ('file1', models.IntegerField(max_length=10, null=True)),
                ('file2', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='hotviewpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewpoint', models.CharField(max_length=50, null=True)),
                ('area', models.CharField(max_length=50, null=True)),
                ('file1', models.IntegerField(max_length=10, null=True)),
                ('file2', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='icno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageurl', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provinceID', models.CharField(max_length=10)),
                ('province', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='sex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=20, unique=True)),
                ('username', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30, null=True)),
                ('birthday', models.DateField(max_length=20, null=True)),
                ('mark', models.IntegerField(null=True)),
                ('content', models.TextField(null=True)),
                ('filed1', models.CharField(max_length=10, null=True)),
                ('filed2', models.CharField(max_length=10, null=True)),
                ('icno', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.icno')),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.login')),
                ('sex', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.sex')),
            ],
        ),
        migrations.AddField(
            model_name='focus',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
