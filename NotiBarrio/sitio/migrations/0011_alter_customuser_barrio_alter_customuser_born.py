# Generated by Django 4.1 on 2022-09-23 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0010_alter_customuser_is_accept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='barrio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sitio.barrio'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='born',
            field=models.DateField(default=None, null=True),
        ),
    ]
