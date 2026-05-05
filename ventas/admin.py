from django.contrib import admin
from .models import (
    Auto, Cargo, Empleado, Cliente, Categoria, 
    Venta, Detalle_Venta, Financiamiento, Pago
)

# Registramos todos los modelos para que aparezcan en el panel /admin/
admin.site.register(Auto)
admin.site.register(Cargo)
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Venta)
admin.site.register(Detalle_Venta)
admin.site.register(Financiamiento)
admin.site.register(Pago)