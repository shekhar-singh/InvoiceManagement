# from django.core import serializers
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Invoice, InvoiceItem


# Create your views here.

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        pdfFile = request.FILES['file']
        instance = Invoice()
        instance.pdfFile = pdfFile
        instance.digitized = False
        instance.save()
        fileId = instance.pk

        return JsonResponse({"message": "updated successfully", "fileId": fileId})
    else:
        return JsonResponse({"message": "something went wrong"})


def getDigitizationStatus(request, fid):
    try:
        invoice = Invoice.objects.get(pk=fid)
        digitized = invoice.digitized

        if digitized:
            status = "digitized"
        else:
            status = "pending"

        return JsonResponse({"status": status})

    except Exception as e:
        return JsonResponse({"status": "No result found"})


def getInvoice(request, fid):
    try:
        invoice = Invoice.objects.get(pk=fid)
        invoice_item = InvoiceItem.objects.filter(invoice=invoice)
        items = list(invoice_item.values())
        invoiceDetails = {'invoiceNumber': invoice.invoiceNumber, 'issueDate': invoice.issueDate,
                          'dueDate': invoice.dueDate, 'total': invoice.total, 'items': items}

        return JsonResponse({"Invoice": invoiceDetails})
    except Exception as e:
        return JsonResponse({"status": "something went wrong"})


@csrf_exempt
def addInvoice(request):
    try:
        if request.method == 'POST':
            json_data = json.loads(request.body)

            fid = json_data["fileId"]
            invoice = Invoice.objects.get(pk=fid)

            invoiceNumber = json_data["invoiceNumber"]
            if invoiceNumber:
                invoice.invoiceNumber = invoiceNumber

            issueDate = json_data["issueDate"]
            if issueDate:
                invoice.issueDate = issueDate

            dueDate = json_data["dueDate"]
            if dueDate:
                invoice.dueDate = dueDate

            total = json_data["total"]
            if total:
                invoice.total = total

            print(invoice.digitized)
            if not invoice.digitized:
                invoice.digitized = False

            invoice.save()
            items = json_data["items"]

            for i in items:
                InvoiceItem.objects.filter(invoice=invoice).update(**i)

            return JsonResponse({"message": "updated successfully"})

    except Exception as e:
        return JsonResponse({"message": "something went wrong"})


@csrf_exempt
def markDigitized(request):
    try:

        if request.method == 'POST':
            json_data = json.loads(request.body)
            file_id = json_data['id']

            invoice = Invoice.objects.get(pk=file_id)
            invoice.digitized = True
            invoice.save()

            digitizedStatus = invoice.digitized
            if digitizedStatus:
                status = "digitized"
            else:
                status = "got some issue"

            return JsonResponse({"status": status})

    except Exception as e:
        return JsonResponse({"status": "something went wrong"})
