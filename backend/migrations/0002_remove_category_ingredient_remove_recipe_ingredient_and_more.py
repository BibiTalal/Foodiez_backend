# Generated by Django 4.1.2 on 2022-12-07 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='category',
            name='ingredients',
            field=models.ManyToManyField(related_name='categories', to='backend.ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='Recipe_ingredients', to='backend.ingredient'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ManyToManyField(related_name='categories', to='backend.category'),
        ),
    ]
