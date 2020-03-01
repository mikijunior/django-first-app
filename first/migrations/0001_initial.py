# Generated by Django 3.0.3 on 2020-03-01 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='article title')),
                ('text', models.TextField(verbose_name='article text')),
                ('pub_date', models.DateTimeField(verbose_name='publish date')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50, verbose_name='comment author')),
                ('comment', models.CharField(max_length=255, verbose_name='comment text')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.Article')),
            ],
        ),
    ]
