from django.test import TestCase
from api.models import Invoice, InvoiceItem
from django.test import Client


# Create your tests here.

class DigitizationTestCase(TestCase):
    def setUp(self):
        Invoice.objects.create(pdfFile="abc.pdf", digitized=False)
        client = Client()

    def test_get_digitization_status(self):
        response = self.client.get('/getDigitizationStatus/1')
        self.assertEqual(response.status_code, 200)

    def test_get_invoice_status(self):
        response = self.client.get('/getInvoice/1')
        invoice = Invoice.objects.get(pk=1)
        digitized = invoice.digitized
        self.assertEqual(response.status_code, 200)
        self.assertEqual(digitized, False)

    def test_mark_digitized(self):
        data = {
            "file_id": 1
        }
        response = self.client.post("/markDigitized/", data=data)
        self.assertEqual(Invoice.objects.count(), 1)

    def test_get_invoice(self):
        response = self.client.post("/getInvoice/1")
        self.assertEqual(response.status_code, 200)

    def test_add_invoice(self):
        data = {
            "invoiceNumber": "inv002",
            "fileId": 1,
            "issueDate": "12 jan 2020",
            "dueDate": "20 jan 2020",
            "total": "10.00",
            "items": [
                {
                    "description": "item1",
                    "quantity": 1,
                    "unitPrice": "5.00",
                    "amount": "5.00"
                },
                {
                    "description": "item2",
                    "quantity": 1,
                    "unitPrice": "5.00",
                    "amount": "5.00"
                }
            ]
        }

        response = self.client.post("/getInvoice/", data=data)
        self.assertEqual(Invoice.objects.count(), 1)



