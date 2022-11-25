#Se crea yna clase para registrar al usuario.
nombre=input('Dime el nombre')
dni=input('Dime el dni')
tlf=input('Dime el número de tlf')
ciudad=input('Dime la ciudad')
correo=input('Dime el correo')
contraseña=input('Dime la contraseña')

print('Usuario registrado')

#Se crea una clase que se llama producto donde se almacena todos los valores.
class Producto:
    def __init__(self, producto, unidad,precio) -> None:#aqui metemos la variable del cliente.
        self.producto=producto
        self.unidad=unidad
        self.precio=precio
    
    def mostrarDetalle(self):
        print(f'El producto {self.producto}, tiene un precio de {self.precio} y hay total de {self.unidad} unidad ')


#Ahora se crea productos distintos.
producto1=Producto('Balón',25,100)
producto2=Producto('Equipación',48,140)
producto3=Producto('Botas',55,110)
producto4=Producto('Espinilleras',68,200)   


#Llamamos al producto para que se vea el detalle de esos productos.
producto1.mostrarDetalle()
producto2.mostrarDetalle()
producto3.mostrarDetalle()
producto4.mostrarDetalle()
   
carrito={}
continuar=True
while continuar:
    producto=input('Selecione los productos que desees ')  
    precio=float(input('Introduce el precio de'+ producto))
    carrito[producto]=precio
    continuar=input('Deseas mas productos a la lista(si/no)')=='si'

#Valor carrito:
coste=0
print('Lista de compra')
for producto, precio in carrito.producto():
    print(producto,'\t',precio)
    coste+=precio
    print('Coste total:',coste)
pago=input('Pagar en cash o tarjeta')
print('El precio se envió al correo')
print('La compra se ha enviado en mensaje sms o correo')






    







 


