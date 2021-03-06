from django.db import models


# Create your models here.
class Invoice(models.Model):
    fileId = models.AutoField(primary_key=True, editable=False)
    pdfFile = models.FileField(blank=False, null=False)
    invoiceNumber = models.CharField(max_length=20, unique=True, blank=True, editable=False, null=True)
    issueDate = models.CharField(max_length=20, blank=True, null=True)
    dueDate = models.CharField(max_length=20, blank=True, null=True)
    digitized = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items', unique=False)
    description = models.TextField(blank=True, default="")
    quantity = models.PositiveIntegerField()
    unitPrice = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
