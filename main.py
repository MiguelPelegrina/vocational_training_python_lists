lista = []
entrada = ""


def darDeBaja():
    codigo = input("Introduzca el código del producto que quiera dar de baja")
    existe = True
    for i in lista:
        if(i.get("Código artículo") == codigo):
            lista.remove(i)
            print("Se ha eliminado el producto con el codigo " + codigo + " de la lista")
            return
        else:
            existe = False
    if(existe == False):
        print("El producto no se encuentra en la lista")


def buscar():
    datoArticulo = input("Introduzca cualquier dato por el cúal quiera buscar un artículo")
    noExiste = False
    for i in lista:
        for clave, valor in i.items():
            if valor == datoArticulo:
                for clave,valor in i.items():
                    noExiste = True
                    print(clave,valor)
    if (noExiste == False):
        print("El producto no se encuentra en la lista")

def modificar():
    codigo = input("Introduzca el código del producto que quiera modificar")
    existe = True
    for i in lista:
        if (i.get("Código artículo") == codigo):
            modificacion = input("¿Qué característica del artículo desea modificar?"
                  "\n 1: Para cambiar el nombre" +
                  "\n 2: Para cambiar la descripcion" +
                  "\n 3: Para cambiar el precio"
                  )
            if modificacion == "1":
                valor = input("¿Cúal será el nuevo nombre?")
                i.update({"Nombre":valor})
            elif modificacion == "2":
                valor = input("¿Cúal será la nueva descripción?")
                i.update({"Descripción":valor})
            elif modificacion == "3":
                valor = input("¿Cúal será el nuevo precio?")
                i.update({"Precio":valor})
        else:
            existe = False
    if (existe == False):
        print("El producto no se encuentra en la lista")


def contieneCodigo(codigo):
    for i in lista:
        if (i.get("Código artículo") == codigo):
            return True
    return False


def darDeAlta():
    cod_articulo = input("Introduzca el código del producto que quiera dar de alta")
    while contieneCodigo(cod_articulo):
        cod_articulo = input("Introduzca el código de un producto que NO esté ya dado de alta")
    nombre = input("Introduzca el nombre del producto")
    descripcion = input("Introduzca la descripcion del producto")
    precio = input("Introduzca el precio del producto")
    diccionario = {"Código artículo": cod_articulo,
                   "Nombre": nombre,
                   "Descripción": descripcion,
                   "Precio": precio
                   }
    lista.append(diccionario)


while entrada != "6":
    entrada = input("Introduzca un numero de 1 a 6: " +
        "\n 1: Para dar un producto de alta" +
        "\n 2: Para dar un producto de baja" +
        "\n 3: Para modificar un el nombre, la descripcion o el precio de un producto" +
        "\n 4: Para buscar en función de una característica" +
        "\n 5: Para listar todos los productos " +
        "\n 6: Para salirse del programa")
    if entrada == "1":
        darDeAlta()
    elif entrada == "2":
        darDeBaja()
    elif entrada == "3":
        modificar()
    elif entrada == "4":
        buscar()
    elif entrada == "5":
        for i in lista:
            for clave, valor in i.items():
                print(clave,valor)