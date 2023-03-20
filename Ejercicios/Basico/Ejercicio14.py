'''
//Programa para calcular el precio de venta de un producto
'''

precio_unidad = float(input("Ingrese el valor por unidad del producto ->"))
cantidad = int(input("Ingrese la cantidad de articulos ->"))
iva = int(input("Ingrese el valor del iva -> "))

preciofinal = (precio_unidad + iva) * cantidad

print("Precio de venta -> ",preciofinal)