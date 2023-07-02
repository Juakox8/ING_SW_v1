# Generated by Django 4.2.1 on 2023-05-30 17:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gestionReservas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hours',
            old_name='hour',
            new_name='time',
        ),
        migrations.RemoveField(
            model_name='hours',
            name='idDay',
        ),
        migrations.AddField(
            model_name='hours',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Days',
        ),
    ]