from django.db import models

class Invoice(models.Model):
    date = models.DateField()
    invoice_no = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name        

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='details', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
