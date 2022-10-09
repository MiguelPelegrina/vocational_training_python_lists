#Declaración e inicialización de variables
lista = []
entrada = ""


# Funciones auxiliares
# Función auxiliar que recorre la lista para comprobar si contiene el código introducido. Devuelve el diccionario si la
# lista contiene el código o devuelve None si no lo contiene
def contieneCodigo(codigo):
    #Recorremos la lista
    for diccionario in lista:
        if (diccionario.get("Código artículo") == codigo):
            return lista.__getitem__(lista.index(diccionario))
    return None


# Función auxiliar para poder ordenar la lista
def obtener_codigo(diccionario):
    return diccionario["Código artículo"]


# Función que permite al usuario dar de alta un artículo en la lista
def darDeAlta():
    cod_articulo = input("Introduzca el código del producto que quiera dar de alta")
    # Se le pedirá al usuario un código de artículo válido hasta que el dato introducido no esté ya dentro de la lista
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


# Función que permite al usuario dar de baja a un producto con su respectivo código de artículo
def darDeBaja():
    # Le pedimos información al usuario
    codigo = input("Introduzca el código del producto que quiera dar de baja")
    # Comprobamos que el código introducido existe
    articulo = contieneCodigo(codigo)
    # Si existe
    if (articulo != None):
        # Eliminamos el diccionario
        lista.remove(articulo)
        print("Se ha eliminado el producto con el codigo " + codigo + " de la lista")
    # Si el artículo no se encuentra en la lista
    else:
        # Se informa al usuario
        print("El producto no se encuentra en la lista")


# Función que permite al usuario ver qué artículos disponen de las características introducidas
def buscar():
    datoArticulo = input("Introduzca cualquier dato por el cúal quiera buscar un artículo")
    # Damos por hecho que existe el producto
    noExiste = False
    # Recorremos la lista
    for i in lista:
        # Recorremos todos los diccionarios de la lista
        for clave, valor in i.items():
            # Si algún valor del mapa corresponde al dato indicado por el usuario
            if valor == datoArticulo:
                for clave,valor in i.items():
                    # Se ha encontrado algún dato
                    noExiste = True
                    # Se saca por pantalla todos los datos del diccionario que coincide con el dato introducido
                    print(clave,valor)
    # Si el dato indicado no se encuentra en toda la lista
    if (noExiste == False):
        print("El producto no se encuentra en la lista")


# Función que modifica
def modificar():
    codigo = input("Introduzca el código del producto que quiera modificar")
    # Comprobamos que existe el producto
    articulo = contieneCodigo(codigo)
    # Recorremos la lista
    modificacion = input("¿Qué característica del artículo desea modificar?"
        "\n 1: Para cambiar el nombre" +
        "\n 2: Para cambiar la descripcion" +
        "\n 3: Para cambiar el precio"
        )
    #Modificamos el nombre
    if modificacion == "1":
        valor = input("¿Cúal será el nuevo nombre?")
        articulo.update({"Nombre":valor})
    #Modificamos la descripción
    elif modificacion == "2":
        valor = input("¿Cúal será la nueva descripción?")
        articulo.update({"Descripción":valor})
    #Modificamos el valor
    elif modificacion == "3":
        valor = input("¿Cúal será el nuevo precio?")
        articulo.update({"Precio":valor})
    else:
        print("Introduzca una respuesta válida")
    # Si no se encuentra ningún producto que coincida con el código indicado
    if (articulo == None):
        print("El producto no se encuentra en la lista")


while entrada != "6":
    # Ordenamos la lista automáticamente en función del código de los artículos 
    lista.sort(key=obtener_codigo)
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
