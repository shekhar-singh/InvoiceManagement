# Generated by Django 3.1.5 on 2021-01-10 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('fileId', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('pdfFile', models.FileField(upload_to='')),
                ('invoiceNumber', models.CharField(blank=True, editable=False, max_length=20, null=True, unique=True)),
                ('issueDate', models.DateTimeField(blank=True, null=True)),
                ('dueDate', models.DateTimeField(blank=True, null=True)),
                ('digitized', models.BooleanField(default=False)),
                ('total', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default='')),
                ('quantity', models.PositiveIntegerField()),
                ('unitPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='api.invoice')),
            ],
        ),
    ]
