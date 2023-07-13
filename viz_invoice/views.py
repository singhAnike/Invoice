from .models import Invoice, InvoiceDetail
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
# here i have used apiview for clearity
class InvoiceDetailInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ['description', 'quantity', 'unit_price', 'price']


class InvoiceOutputSerializer(serializers.ModelSerializer):
    details = InvoiceDetailInputSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ['customer_name', 'date', 'invoice_no', 'details']


class InvoiceAPIView(APIView):
    def get(self, request):
        invoices = Invoice.objects.all()
        serializer = InvoiceOutputSerializer(invoices, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = InvoiceOutputSerializer(data=request.data)
        if serializer.is_valid():
            details_data = serializer.validated_data.pop('details')
            invoice = Invoice.objects.create(**serializer.validated_data)

            for detail_data in details_data:
                InvoiceDetail.objects.create(invoice=invoice, **detail_data)

            response_serializer = InvoiceOutputSerializer(invoice)
            return Response(response_serializer.data)
        return Response(serializer.errors, status=400)
