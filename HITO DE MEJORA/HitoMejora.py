from datetime import datetime

class Cliente:
    def __init__(self, nombre, apellidos, direccion, correo, telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.correo = correo
        self.telefono = telefono
    
    def registrar(self):
        # Validar datos del cliente
        # Guardar cliente en la base de datos
        print("Cliente bien registrado")

class Pedidos:
    def __init__(self,cliente,producto,precio,IVA):
        self.cliente=cliente 
        self.producto=producto
        self.precio=precio
        self.IVA=IVA
    def calcular_precio_final(self):
        return self.precio * (1+self.IVA)

    def imprimir_facturaPDF(self):
        print('factura enviada en pdf')

class Producto:
    def __init__(self,id,nombre,unidades,precio,fecha_alta):
        self.id=id
        self.nombre=nombre
        self.unidades=unidades
        self.precio=precio #number, entero o decimales
        self.fecha_alta=fecha_alta #fecha : utilizar clase datetime
    def fichaProducto(self):
        print(f'El dato del producto es {self.nombre}')

#Crear un nuevo cliente
cliente1=Cliente('javier','Ahijado Luna','javier@gmail.com','Leganes','675-84-88-57')
   
#Registar al Cliente
cliente1.registrar()

#Crear un nuevo pedido
pedido1=Pedidos(cliente1,"Producto",2,"tarjeta de credito")

#Imprimir factura de pedido
pedido1.imprimir_facturaPDF()


