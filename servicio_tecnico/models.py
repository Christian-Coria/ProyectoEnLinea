from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.html import format_html


class Cliente(models.Model):

    nombre_completo = models.CharField(max_length=80)
    telefono = PhoneNumberField(unique = True, null = False, blank = False)
    
    def __str__(self):
        return self.nombre_completo


class Reparacion(models.Model):
    Motorola = 'Motorola',
    Samsung = 'Samsung',
    Lg = 'Lg',
    Xiaomi = 'Xiaomi',
    Alcatel = 'Alcatel',
    Huawey = 'Huawey',
    Chino = 'Chino',
    Iphone = 'Iphone',
    MARCA = (
        ('Motorola','Motorola'),
        ('Samsung','Samsung'),
        ('Lg','Lg'),
        ('Xiaomi','Xiaomi'),
        ('Sony','Sony'),
        ('Huawey','Huawey'),
        ('Chino','Chino'),
        ('Otro','Otro'),
    )

    Pendiente = 'Pendiente',
    Aceptado = 'Aceptado',
    Reparado = 'Reparado',
    Irreparable = 'Irreparable',
    Entregado = 'Entregado',
    Entregado_Irreparable = 'Entregado Irreparable',
    ESTADO = (
        ('Pendiente','Pendiente'),
        ('Aceptado','Aceptado'),
        ('Reparado','Reparado'),
        ('Irreparable','Irreparable'),
        ('Entregado','Entregado'),
        ('Entregado Irreparable','Entregado Irreparable'),
        
    )

    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente,null=True, on_delete=models.CASCADE)
    marca = models.CharField(max_length=40, choices=MARCA)
    modelo = models.CharField(max_length=40, blank=True)
    imei = models.CharField(max_length=40,blank=True )
    falla = models.TextField(null=False)
    imagen = models.ImageField(upload_to="fallas//%Y/%m/%d", null=True, blank=True)   
    comentarios = models.TextField(null=True, blank=True)
    presupuesto = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    pago_seña = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    precio = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=40, choices=ESTADO, default='Pendiente')
    
    def tipo_de_reparacion(self):   #el metodo se agrega en el admin.py -- La misma logica se puede trabajar en cualquier atributo de instancia
        if self.estado == 'Pendiente':
            return format_html('<spam style="background-color: #5DF707; padding:7px;">{}</spam>', self.estado ) # le damos color a estado en el html
        elif self.estado == 'Aceptado':
            return format_html('<spam style="background-color: #f0f; padding:7px;">{}</spam>',  self.estado)
        elif self.estado == 'Reparado':
            return format_html('<spam style="background-color: #D9AD04; padding:7px;">{}</spam>',  self.estado)
        elif self.estado == 'Irreparable':
            return format_html('<spam style="background-color: #099; padding:7px">{}</spam>',  self.estado)
        elif self.estado == 'Entregado':
            return format_html('<spam style="background-color: #31B009; padding:7px">{}</spam>',  self.estado)
        elif self.estado == 'Entregado Irreparable':
            return format_html('<spam style="background-color: #f00; padding:7px">{}</spam>',  self.estado)




    def __str__(self):
            return ''


class Proveedores(models.Model):
    nombre = models.CharField(max_length=40)
    telefono = PhoneNumberField(unique = True, null = False, blank = False)
   
    def __str__(self):
        return f'Proveedor {self.nombre}: {self.telefono}'

        

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)