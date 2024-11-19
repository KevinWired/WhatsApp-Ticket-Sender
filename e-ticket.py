'''

    date: Nov 14, 2024
    
    autor: Kevin Santillan

    file: e-ticket.py

'''

from collections import namedtuple
from datetime import datetime
import pywhatkit as kit
import emoji

Producto = namedtuple("Producto", ["nombre", "valor", "cantidad"])
shopping_cart = []

def add_item():
    nombre = input("Nombre del producto: ").capitalize()
    valor = float(input("Valor del producto ($): "))
    cantidad = int(input("Cantidad: "))
    producto = Producto(nombre, valor, cantidad)
    shopping_cart.append(producto)
    print("Producto agregado.\n")

def delete_item():
    nombre = input("Nombre del producto a eliminar: ").capitalize()
    for producto in shopping_cart:
        if producto.nombre == nombre:
            shopping_cart.remove(producto)
            print("Producto eliminado.\n")
            return
    print("Producto no encontrado.\n")

def reconfig():
    nombre = input("Nombre del producto a ajustar: ").capitalize()
    for i, producto in enumerate(shopping_cart):
        if producto.nombre == nombre:
            nuevo_valor = float(input("Nuevo valor del producto ($): "))
            nueva_cantidad = int(input("Nueva cantidad: "))
            shopping_cart[i] = Producto(nombre, nuevo_valor, nueva_cantidad)
            print("Producto ajustado.\n")
            return
    print("Producto no encontrado.\n")

def items_dump():
    if not shopping_cart:
        print("No hay productos en la lista.\n")
        return
    print("Productos en la lista:")
    for producto in shopping_cart:
        print(f"Producto: {producto.nombre}, Valor: ${producto.valor:.2f}, Cantidad: {producto.cantidad}")
    print()

def total():
    total = 0
    for producto in shopping_cart:
        total += producto.valor * producto.cantidad
    return total

def send_ticket():
    country = "+54"
    number = input("Ingresa el número de WhatsApp del cliente: ")
    number_validation = input("Volve a ingresar el numero de WhatsApp: ")
    present_time = datetime.now()
    date = present_time.strftime("%d/%m/%Y")

    while number != number_validation:
        print("Los numeros no coinciden. Vuelve a ingresar el numero de WhatsApp.")
        number = input("Ingresa el numero de WhatsApp del cliente: ")
        number_validation = input("Volve a ingresar el numero de WhatsApp: ")

    full_number = country + number

    mensaje = emoji.emojize(f"Kevin Santillan :rocket:\n Fecha: {date} :spiral_calendar:\n Detalles de su compra :ticket:\n---\n")
    for producto in shopping_cart:
        mensaje += f"Producto: {producto.nombre}, Valor: ${producto.valor:.2f}, Cantidad: {producto.cantidad}\n"
    mensaje += f"---\nTotal: ${total():.2f} \n\n ¡Gracias por su compra!\n"
    
    wait_time = 15
    tab_close = False
    close_time = 3

    kit.sendwhatmsg_instantly(full_number, mensaje, wait_time, tab_close, close_time)

def new_ticket():
    global shopping_cart
    shopping_cart = []
    print("Nuevo ticket generado.\n")

def main():
    while True:
        print("<1> Agregar producto")
        print("<2> Eliminar producto")
        print("<3> Editar un producto")
        print("<4> Ver lista de productos")
        print("<5> Enviar ticket")
        print("<6> Nuevo ticket")
        print("<7> Salir\n")
        choice = input("Marque una opción: ")
        if choice == "1":
            add_item()
        elif choice == "2":
            delete_item()
        elif choice == "3":
            reconfig()
        elif choice == "4":
            items_dump()
        elif choice == "5":
            send_ticket()
        elif choice == "6":
            new_ticket()
        elif choice == "7":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.\n")

if __name__ == "__main__":
    main()
