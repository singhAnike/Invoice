from django.contrib import admin
from viz_invoice.models import Invoice, InvoiceDetail

admin.site .register(Invoice)
admin.site.register(InvoiceDetail)