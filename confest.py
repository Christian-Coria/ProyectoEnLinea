import pytest
from product.models import Producto
from django.contrib.auth.models import User
import datetime
from faker import Faker
fake = Faker()
from pruduct.models import Categoria

@pytest.fixture()
def crear_producto(db):   # se pasa el parametro db para acceder con la fixture a la base de datos 
    mi_producto = Producto(producto = "Producto 4", fecha_publicacion= datetime.datetime.now())
    mi_producto.save()
    return mi_producto



# factories permiten hacer fixtures complejos y mayor control de clases de modelos 
@pytest.fixture
def crear_producto_factory(db):
    categoria1 = Categoria(nombre="Cat", slug="cat")
    categoria1.save()
    def crear_producto(
        estado: str="Borrador",
        producto: str= "Producto 1",
        fecha_publicacion = datetime.datetime.now(),
        imagen: str="ruta",
        categoria = categoria1,
    ):
        mi_producto = Producto(
            estado = estado,
            producto = producto,
            fecha_publicacion = fecha_publicacion,
            imagen = imagen,
            categoria = categoria,
        )
        mi_producto.save()
        return mi_producto
    return crear_producto

@pytest.fixture()
def producto(db, crear_producto_factory):
    return crear_producto_factory("Borrador",fake.name(), fake.date(), fake.file_path())