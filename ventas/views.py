from django.shortcuts import render
from .models import Auto, Venta, Cliente, Categoria

def dashboard(request):
    # Contamos cuántos registros hay en cada tabla
    total_autos = Auto.objects.count()
    total_ventas = Venta.objects.count()
    total_clientes = Cliente.objects.count()
    
    # Pasamos los datos a la página web (el template)
    context = {
        'total_autos': total_autos,
        'total_ventas': total_ventas,
        'total_clientes': total_clientes,
    }
    return render(request, 'ventas/dashboard.html', context)