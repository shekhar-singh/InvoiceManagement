# Generated by Django 3.1.5 on 2021-01-10 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='dueDate',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='issueDate',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
