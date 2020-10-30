# Generated by Django 3.0.8 on 2020-07-14 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Big',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_hot', models.BooleanField(default=False)),
                ('is_old', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Middle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_hot', models.BooleanField(default=False)),
                ('is_old', models.BooleanField(default=False)),
                ('big_theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='middles', to='map.Big')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_hot', models.BooleanField(default=False)),
                ('is_old', models.BooleanField(default=False)),
                ('middle_theme', models.ManyToManyField(blank=True, related_name='stock', to='map.Middle')),
            ],
        ),
        migrations.CreateModel(
            name='StockComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='map.Stock')),
            ],
        ),
        migrations.CreateModel(
            name='MiddleComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('middle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='map.Middle')),
            ],
        ),
        migrations.CreateModel(
            name='BigComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('big', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='map.Big')),
            ],
        ),
    ]
