from django.shortcuts import render
from api.models import Invoice, InvoiceItem
from django.http import JsonResponse
# from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def upload():
    pass

def getDigitizationStatus(request, fid):
    try:
        invoice = Invoice.objects.get(pk = fid)
        digitized = invoice.digitized

        if digitized:
            status = "digitized"
        else:
            status = "pending"

        return JsonResponse({"status":status})

    except Exception as e:
        raise e
        return JsonResponse({"status":"someting went wrong"})

    

def getInvoice(request,fid):
    try:
        invoice = Invoice.objects.get(pk = fid)
        invoice_item = InvoiceItem.objects.filter(invoice = invoice)
        items = list(invoice_item.values())
        invoiceDetails = {}
        invoiceDetails['invoiceNumber'] = invoice.invoiceNumber
        invoiceDetails['issueDate'] = invoice.issueDate
        invoiceDetails['dueDate'] = invoice.dueDate
        invoiceDetails['total'] = invoice.total
        invoiceDetails['items'] = items

        print(invoiceDetails)
    
        return JsonResponse({"Invoice":invoiceDetails})
    except Exception as e:
        # raise e
        print(e)
    # finally:
    #     return JsonResponse({"status":"someting went wrong"})
    
@csrf_exempt
def addInvoice(request):
    try:
        if request.method == 'POST':
            json_data=json.loads(request.body)
            print(json_data)
            # import pdb; pdb.set_trace()
            fid = json_data["fileId"]
            invoice = Invoice.objects.get(pk = fid)

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

            # invoice_id = json_data["invoice_id"]
            items = json_data["items"]

            for i in items:
                invoice_item = InvoiceItem.objects.filter(invoice = invoice).update(**i)


            return JsonResponse({"message":"updated successfully"})




    except Exception as e:
        raise e
        return JsonResponse({"message":"something went wrong"})

@csrf_exempt
def markDigitized(request):
    try:

        if request.method == 'POST':
            json_data=json.loads(request.body)
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
            pass
    except Exception as e:
        raise e
    finally:
        return JsonResponse({"status":"someting went wrong"})
