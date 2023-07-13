from django.test import TestCase
from rest_framework.test import APIClient
from .models import Invoice, InvoiceDetail

# here i am writing s simple testcase to test api 
class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_invoice(self):
        # Define the input data for creating an invoice
        input_data = {
            'customer_name': 'Aniket singh',
            'date': '2023-07-13',
            'invoice_no': 'INV-123',
            'details': [
                {
                    'description': 'Product 1',
                    'quantity': 20,
                    'unit_price': 10.99,
                    'price': 21.98
                },
                {
                    'description': 'Product 2',
                    'quantity': 1,
                    'unit_price': 5.99,
                    'price': 5.99
                }
            ]
        }

        response = self.client.post('/api/invoices/', input_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Invoice.objects.count(), 1)
        self.assertEqual(InvoiceDetail.objects.count(), 2)

        expected_output = {
            'customer_name': 'Aniket singh',
            'date': '2023-07-13',
            'invoice_no': 'INV-123'
        }
        self.assertEqual(response.data, expected_output)

# here this testcase is not working becouse in my views.py i used 200(ok) status code but here
# i have mentioned 201(created) status code 
# So this is a simple way to test our api views...

