import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Invoice, InvoiceItem


# Create your views here.

@csrf_exempt
def upload(request):
    try:
        if request.method == 'POST':
            document = request.FILES['file']
            if not request.FILES['file']:
                return JsonResponse({"message": "Please upload a valid document"})

            instance = Invoice()
            instance.pdfFile = document
            instance.digitized = False
            instance.save()
            fileId = instance.pk

            return JsonResponse({"message": "updated successfully", "fileId": fileId})
    except Exception as e:
        return JsonResponse({"message": "something went wrong"})


def getDigitizationStatus(request, file_id):
    try:
        invoice = Invoice.objects.get(pk=file_id)
        digitized = invoice.digitized

        if digitized:
            status = "digitized"
        else:
            status = "pending"

        return JsonResponse({"status": status})

    except Exception as e:
        return JsonResponse({"status": "No result found!"})


def getInvoice(request, file_id):
    try:
        invoice = Invoice.objects.get(pk=file_id)
        digitized = invoice.digitized

        if not digitized:
            status = "pending"
            return JsonResponse({"status": status})
            
        invoice_item = InvoiceItem.objects.filter(invoice=invoice)
        items = list(invoice_item.values('description','quantity','unitPrice','amount'))
        invoiceDetails = {'invoiceNumber': invoice.invoiceNumber, 'issueDate': invoice.issueDate,
                          'dueDate': invoice.dueDate, 'total': invoice.total, 'items': items}

        return JsonResponse({"Invoice": invoiceDetails})
    except Exception as e:
        return JsonResponse({"status": "No result found!"})


@csrf_exempt
def addInvoice(request):
    try:
        if request.method == 'POST':
            json_data = json.loads(request.body)

            file_id = json_data["fileId"]
            if not file_id:
                return JsonResponse({"message": "Please enter a valid file id !"})

            invoice = Invoice.objects.get(pk=file_id)

            invoiceNumber = json_data["invoiceNumber"]
            if json_data["invoiceNumber"]:
                invoice.invoiceNumber = invoiceNumber

            issueDate = json_data["issueDate"]
            if json_data["issueDate"]:
                invoice.issueDate = issueDate

            dueDate = json_data["dueDate"]
            if json_data["dueDate"]:
                invoice.dueDate = dueDate

            total = json_data["total"]
            if json_data["total"]:
                invoice.total = total

            if not invoice.digitized:
                invoice.digitized = False

            invoice.save()
            items = json_data["items"]

            for item in items:
                InvoiceItem.objects.filter(invoice=invoice).update(**item)

            return JsonResponse({"message": "updated successfully"})

    except Exception as e:
        return JsonResponse({"message": "something went wrong"})


@csrf_exempt
def markDigitized(request):
    try:

        if request.method == 'POST':
            json_data = json.loads(request.body)
            file_id = json_data['file_id']

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
