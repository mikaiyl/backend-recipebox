# Generated by Django 2.1.7 on 2019-03-08 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipebox', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='food_id',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='food',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipebox.Food'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipebox.Unit'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='total_time',
            field=models.DurationField(),
        ),
    ]
