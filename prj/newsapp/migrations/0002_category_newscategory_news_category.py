# Generated by Django 4.1.6 on 2023-02-10 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('subscribes', models.ManyToManyField(related_name='categories', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsapp.category')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsapp.news')),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ManyToManyField(through='newsapp.NewsCategory', to='newsapp.category'),
        ),
    ]
