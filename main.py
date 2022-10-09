lista = []
entrada = ""
esValido = False

#def darDeBaja(codigo):
    #for i in lista:

#def buscar

def contieneCodigo(codigo):
    contiene = False
    #NO ESTÁ BIEN TODAVÍA, ME DEBE A
    for i in lista:
        for clave, valor in i.items():
            if valor == codigo:
                contiene = True
    return contiene

def darDeAlta():
    cod_articulo = input("Introduzca el código del producto que quiera dar de alta")
    while contieneCodigo(cod_articulo):
        cod_articulo = input("Introduzca el código de un producto que NO esté ya dado de alta")
    nombre = input("Introduzca el nombre del producto")
    descripcion = input("Introduzca la descripcion del producto")
    precio = input("Introduzca el precio del producto")
    diccionario = {"Código artículo": cod_articulo,
                   "Nombre": nombre,
                   "Descripcion": descripcion,
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
        codigoArticulo = input("Introduzca el código del producto que quiera dar de baja")
        #darDeBaja(codigoArticulo)
    elif entrada == "3":
        codigoArticulo = input("Introduzca el código del producto que quiera modificar")
    elif entrada == "5":
        for i in lista:
            for clave, valor in i.items():
                print(clave,valor)
            print("\n")



