from django.db import models

# 1. Categorías de vehículos
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self): return self.nombre

# 2. Cargos de trabajo
class Cargo(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self): return self.nombre

# 3. Datos de Empleados
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    def __str__(self): return self.nombre

# 4. Inventario de Autos
class Auto(models.Model):
    vin = models.CharField(max_length=17, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self): return f"{self.marca} {self.modelo}"

# 5. Datos de Clientes
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    ci = models.CharField(max_length=15, unique=True) 
    telefono = models.CharField(max_length=20)
    def __str__(self): return self.nombre

# 6. Registro de Ventas
class Venta(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self): return f"Venta {self.id} - {self.auto}"

# 7. Detalles adicionales
class Detalle_Venta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

class Financiamiento(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    cuotas = models.IntegerField()

class Pago(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField(auto_now_add=True)