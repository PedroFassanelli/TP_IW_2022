# Generated by Django 4.1 on 2022-08-31 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0004_alter_customuser_barrio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='barrio',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sitio.barrio'),
        ),
    ]