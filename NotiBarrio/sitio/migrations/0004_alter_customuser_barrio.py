# Generated by Django 4.1 on 2022-08-31 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0003_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='barrio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='sitio.barrio'),
        ),
    ]
