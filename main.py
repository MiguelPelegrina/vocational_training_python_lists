lista = []
entrada = ""


def darDeBaja():
    codigo = input("Introduzca el código del producto que quiera dar de baja")
    #Damos por hecho que existe el producto indicado
    existe = True
    #Recorremos la lista
    for i in lista:
        #Si algún diccionario de la lista contiene el código indicado
        if(i.get("Código artículo") == codigo):
            #Eliminamos el diccionario
            lista.remove(i)
            print("Se ha eliminado el producto con el codigo " + codigo + " de la lista")
            #Y nos salimos de la función sin tener que recorrer el resto de la lista
            return
        #Si el código del artículo no se ha encontrado en este diccionario
        else:
            existe = False
    #Si al recorrer la lista entera no se ha encontrado el producto se informa al usuario
    if(existe == False):
        print("El producto no se encuentra en la lista")


def buscar():
    datoArticulo = input("Introduzca cualquier dato por el cúal quiera buscar un artículo")
    #Damos por hecho que existe el producto
    noExiste = False
    #Recorremos la lista
    for i in lista:
        #Recorremos todos los diccionarios de la lista
        for clave, valor in i.items():
            #Si algún valor del mapa corresponde al dato indicado por el usuario
            if valor == datoArticulo:
                for clave,valor in i.items():
                    #Se ha encontrado algún dato
                    noExiste = True
                    #Se saca por pantalla todos los datos del diccionario que coincide con el dato introducido
                    print(clave,valor)
    #Si el dato indicado no se encuentra en toda la lista
    if (noExiste == False):
        print("El producto no se encuentra en la lista")


def modificar():
    codigo = input("Introduzca el código del producto que quiera modificar")
    #Damos por hecho que existe el producto
    existe = True
    #Recorremos la lista
    for i in lista:
        #Si el diccionario corresponde al codigo introducido
        if (i.get("Código artículo") == codigo):
            modificacion = input("¿Qué característica del artículo desea modificar?"
                  "\n 1: Para cambiar el nombre" +
                  "\n 2: Para cambiar la descripcion" +
                  "\n 3: Para cambiar el precio"
                  )
            #Modificamos el nombre
            if modificacion == "1":
                valor = input("¿Cúal será el nuevo nombre?")
                i.update({"Nombre":valor})
            #Modificamos la descripción
            elif modificacion == "2":
                valor = input("¿Cúal será la nueva descripción?")
                i.update({"Descripción":valor})
            #Modificamos el valor
            elif modificacion == "3":
                valor = input("¿Cúal será el nuevo precio?")
                i.update({"Precio":valor})
        else:
            existe = False
    #Si no se encuentra ningún producto que coincida con el código indicado
    if (existe == False):
        print("El producto no se encuentra en la lista")


#Recorremos la lista para saber si la lista con tiene el código introducido
def contieneCodigo(codigo):
    #Recorremos la lista
    for i in lista:
        if (i.get("Código artículo") == codigo):
            return True
    return False


def darDeAlta():
    cod_articulo = input("Introduzca el código del producto que quiera dar de alta")
    #Comprobamos que el código no exista ya
    while contieneCodigo(cod_articulo):
        cod_articulo = input("Introduzca el código de un producto que NO esté ya dado de alta")
    #Le solicitamos el resto de los datos al usuario
    nombre = input("Introduzca el nombre del producto")
    descripcion = input("Introduzca la descripcion del producto")
    precio = input("Introduzca el precio del producto")
    diccionario = {"Código artículo": cod_articulo,
                   "Nombre": nombre,
                   "Descripción": descripcion,
                   "Precio": precio
                   }
    #Añadimos el diccionario a la lista
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