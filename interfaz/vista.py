
import dao.crud as crud
from model.producto import *
from colorama import Fore, Style # type: ignore
from colorama import Fore, Style

def mostrar_menu():    
    print(Style.BRIGHT + Fore.BLUE +
          "\n╔═════════════════════════════════════════════════════════════════════╗\n"
          "║                            📋  MENÚ PRINCIPAL  📋                            ║\n"
          "╠═════════════════════════════════════════════════════════════════════╣\n"
          "║  1. Registrar Producto                                              ║\n"
          "║  2. Mostrar Producto                                                ║\n"
          "║  3. Mostrar Productos                                               ║\n"
          "║  4. Actualizar Producto                                             ║\n"
          "║  5. Eliminar Producto                                               ║\n"
          "║  6. Reportar Bajo Stock de x Producto                               ║\n"
          "║  7. Listar Productos de una Categoría                               ║\n"
          "║  8. Salir                                                           ║\n"
          "╚═════════════════════════════════════════════════════════════════════╝\n"
          + Style.RESET_ALL
    )

def ingresar_opcion():
    opcion = int(input(f"{Fore.GREEN}\nIngrese una opción válida: {Style.RESET_ALL}"))
    opcion_correcta = validar_opcion(opcion)
    return opcion_correcta

def registrar_un_producto():
    print(Style.BRIGHT + Fore.CYAN +
          "\n╔════════════════════════════════════════════════════════════╗\n"
          "║                🆕  REGISTRAR NUEVO PRODUCTO  🆕                 ║\n"
          "╚════════════════════════════════════════════════════════════╝\n"
          + Style.RESET_ALL
    )
    nombre = input(f"{Fore.GREEN}\nIngrese el nombre del producto: {Style.RESET_ALL}")
    nombre = convertir_palabra_correcta(nombre)
    nombre_registrado = crud.buscar_producto_por_nombre(nombre)  
    if nombre_registrado:
        print(Fore.RED +
              "\n╔═══════════════════════════════════════════════════════════════╗\n"
              f"║  ❌  El nombre del producto ingresado ya está registrado.  ❌  ║\n"
              "╚═════════════════════════════════════════════════════════════════╝\n" 
              + Style.RESET_ALL)
    else:
        descripcion = input(f"{Fore.GREEN}\nIngrese una descripción para el producto: {Style.RESET_ALL}")
        descripcion = convertir_palabra_correcta(descripcion)
        precio = float(input(f"{Fore.GREEN}\nIngrese el precio del producto: {Style.RESET_ALL}"))
        precio_correcto = validar_precio(precio)
        cantidad = int(input(f"{Fore.GREEN}\nIngrese la cantidad de unidades del producto: {Style.RESET_ALL}"))
        cantidad_correcta = validar_cantidad(cantidad)
        categoria = input(f"{Fore.GREEN}\nPor favor ingrese la categoría del producto: {Style.RESET_ALL}")
        categoria = convertir_palabra_correcta(categoria)
        
        producto = Producto(nombre, descripcion, precio_correcto, cantidad_correcta, categoria)
        crud.registrar_producto(producto)
        print(Fore.BLUE +
              "\n╔══════════════════════════════════════════════════════╗\n"
              "║       🎉  ¡PRODUCTO REGISTRADO! EXITOSAMENTE: 🎉       ║\n"
              "╚════════════════════════════════════════════════════════╝\n" 
              + Style.RESET_ALL
        )
        
def buscar_producto():
    print(Style.BRIGHT + Fore.CYAN +
        "\n╔════════════════════════════════════════════════════╗\n"
        "║          🔍  BUSCAR PRODUCTO POR CAMPO  🔍          ║\n"
        "╚════════════════════════════════════════════════════╝\n" 
        + Style.RESET_ALL
    )    
    campo_a_buscar = elegir_campo()
    if campo_a_buscar == 1:
        id = int(input(f"{Fore.GREEN}\nIngrese el ID del producto que desea ver: "))
        id = validar_id(id)
        resultado = crud.buscar_producto_por_campo("id", id)
    elif campo_a_buscar == 2:
        nombre = input(f"{Fore.GREEN}\nIngrese el nombre del producto que desea ver: ")
        nombre = convertir_palabra_correcta(nombre)
        resultado = crud.buscar_producto_por_campo("nombre", nombre)
    else:
        categoria = input(f"{Fore.GREEN}\nIngrese la categoría del producto que desea ver: ")
        categoria = convertir_palabra_correcta(categoria)
        resultado = crud.buscar_producto_por_campo("categoria", categoria)

    if resultado:
        print(Fore.BLUE +
              "\n╔════════════════════════════════════════════════════╗\n"
              "║       🎉  ¡PRODUCTO ENCONTRADO! DETALLES: 🎉       ║\n"
              "╚════════════════════════════════════════════════════╝\n" 
              + Style.RESET_ALL
        )
        producto = Producto(id=resultado[0], nombre=resultado[1], descripcion=resultado[2], precio=resultado[3], cantidad=resultado[4], categoria=resultado[5])
        print(producto)
    else:
        print(Fore.RED +
              "\n╔════════════════════════════════════════════════════╗\n"
              f"║  ❌  No se encontró un producto con los datos ingresados.  ❌  ║\n"
              "╚════════════════════════════════════════════════════╝\n" 
              + Style.RESET_ALL
        )
      
def mostrar_productos():
    print(Style.BRIGHT + Fore.BLUE +
          "\n╔═════════════════════════════════════════════════════════════════════╗\n"
          "║                        📋  LISTADO DE PRODUCTOS  📋                         ║\n"
          "╚═════════════════════════════════════════════════════════════════════╝\n" 
          + Style.RESET_ALL
    )    
    resultados = crud.buscar_productos()
    if resultados:
        for prod in resultados:
            producto = Producto(id=prod[0], nombre=prod[1], descripcion=prod[2], precio=prod[3], cantidad=prod[4], categoria=prod[5])
            print(Fore.GREEN +
                  "\n╔═════════════════════════════════════════════════════════════════════╗\n"
                  f"║  Producto ID: {producto.id}                                          ║\n"
                  "╠═════════════════════════════════════════════════════════════════════╣\n"
                  f"║  Nombre: {producto.nombre}                                          ║\n"
                  f"║  Descripción: {producto.descripcion}                                ║\n"
                  f"║  Precio: ${producto.precio}                                         ║\n"
                  f"║  Cantidad: {producto.cantidad}                                      ║\n"
                  f"║  Categoría: {producto.categoria}                                    ║\n"
                  "╚═════════════════════════════════════════════════════════════════════╝\n" 
                  + Style.RESET_ALL
            )
    else:
        print(Fore.RED +
              "\n╔═════════════════════════════════════════════════════════════════════╗\n"
              "║                       ❌  NO HAY PRODUCTOS REGISTRADOS  ❌                       ║\n"
              "╚═════════════════════════════════════════════════════════════════════╝\n" 
              + Style.RESET_ALL
        )
   
def actualizar_producto():
    print(Style.BRIGHT + Fore.CYAN +
          "\n╔════════════════════════════════════════════════════════════╗\n"
          "║               ✏️  ACTUALIZAR PRODUCTO EXISTENTE  ✏️               ║\n"
          "╚════════════════════════════════════════════════════════════╝\n"
          + Style.RESET_ALL
    )
    id = int(input(f"{Fore.GREEN}\nIngrese el ID del producto que desea actualizar: {Style.RESET_ALL}"))
    id = validar_id(id)
    resultado = crud.buscar_producto_por_id(id)  
    if resultado:
        producto = Producto(id=resultado[0], nombre=resultado[1], descripcion=resultado[2], precio=resultado[3], cantidad=resultado[4], categoria=resultado[5])
        cantidad = int(input(f"{Fore.GREEN}\nIngrese la nueva cantidad del producto: {Style.RESET_ALL}"))
        verificar_cantidad = validar_cantidad(cantidad)
        producto.cambiar_cantidad = verificar_cantidad
        crud.actualizar_producto(producto.cantidad, producto.id)
        print(Fore.BLUE +
              "\n╔═══════════════════════════════════════════════════════╗\n"
              "║       🎉  ¡PRODUCTO ACTUALIZADO! EXITOSAMENTE: 🎉       ║\n"
              "╚═════════════════════════════════════════════════════════╝\n" 
              + Style.RESET_ALL
        )       
    else:
        print(Fore.RED +
              "\n╔═══════════════════════════════════════════════════════════════╗\n"
              f"║  ❌  No se encontró el producto especificado.  ❌              ║\n"
              "╚═════════════════════════════════════════════════════════════════╝\n" 
              + Style.RESET_ALL)

def eliminar_producto():
    print(Style.BRIGHT + Fore.RED +
          "\n╔════════════════════════════════════════════════════════════╗\n"
          "║                  🗑️  ELIMINAR PRODUCTO EXISTENTE  🗑️                   ║\n"
          "╚════════════════════════════════════════════════════════════╝\n"
          + Style.RESET_ALL
    )
    id = int(input(f"{Fore.GREEN}\nIngrese el ID del producto que desea eliminar: {Style.RESET_ALL}"))
    id = validar_id(id)
    eliminado = crud.eliminar_producto_por_id(id)
    if eliminado > 0:
        print(Fore.BLUE +
              "\n╔═══════════════════════════════════════════════════════╗\n"
              "║       🎉  ¡PRODUCTO ELIMINADO! EXITOSAMENTE: 🎉         ║\n"
              "╚═════════════════════════════════════════════════════════╝\n" 
              + Style.RESET_ALL
        )
    else:
        print(Fore.RED +
              "\n╔══════════════════════════════════════════════════════════════════════════════╗\n"
              f"║  ❌  No se logró eliminar el producto con el id específicado  ❌              ║\n"
              "╚════════════════════════════════════════════════════════════════════════════════╝\n" 
              + Style.RESET_ALL)

def reportar_bajo_stock():
    print(Style.BRIGHT + Fore.YELLOW +
          "\n╔════════════════════════════════════════════════════════════╗\n"
          "║           📉  REPORTAR PRODUCTOS CON BAJO STOCK  📉            ║\n"
          "╚════════════════════════════════════════════════════════════╝\n"
          + Style.RESET_ALL
    )
    stock = int(input(f"{Fore.BLUE}\nIngrese una cantidad de stock para mostrar los productos por debajo de este: {Style.RESET_ALL}"))
    stock = validar_cantidad(stock)
    resultados = crud.listar_productos_bajo_stock(stock)   
    print(Fore.BLUE + "\n" + ("-") * 25 + " Listado de Productos con Bajo Stock " + ("-" * 25) + "\n" + Style.RESET_ALL)
    if resultados:
        for prod in resultados:
            producto = Producto(id=prod[0], nombre=prod[1], descripcion=prod[2], precio=prod[3], cantidad=prod[4], categoria=prod[5])
            print(Fore.GREEN +
                  "\n╔═════════════════════════════════════════════╗\n"
                  f"║  Producto ID: {producto.id}                           ║\n"
                  f"║  Nombre: {producto.nombre}                     ║\n"
                  f"║  Cantidad: {producto.cantidad}                ║\n"
                  "╚═════════════════════════════════════════════╝\n" 
                  + Style.RESET_ALL
            )
    else:
        print(Fore.RED +
              "\n╔═══════════════════════════════════════════════════════════════╗\n"
              f"║  ❌  No hay productos con bajo stock.  ❌                      ║\n"
              "╚═════════════════════════════════════════════════════════════════╝\n" 
              + Style.RESET_ALL)

def listar_productos_categoria():
    print(Style.BRIGHT + Fore.BLUE +
          "\n╔════════════════════════════════════════════════════════════════════════════╗\n"
          "║                        📋  LISTADO DE CATEGORÍAS  📋                         ║\n"
          "╚══════════════════════════════════════════════════════════════════════════════╝\n" 
          + Style.RESET_ALL
    )
    categoria = input(f"{Fore.BLUE}\nIngrese una categoría de productos: {Style.RESET_ALL}")
    categoria = convertir_palabra_correcta(categoria)
    resultados = crud.listar_productos_por_categoria(categoria)
    print(Fore.BLUE + "\n" + ("-") * 25 + " Listado de Productos Por Categoría " + ("-" * 25) + "\n" + Style.RESET_ALL)
    if resultados:
        for prod in resultados:
            producto = Producto(id=prod[0], nombre=prod[1], descripcion=prod[2], precio=prod[3], cantidad=prod[4], categoria=prod[5])
            print(Fore.GREEN +
                  "\n╔═════════════════════════════════════════════════════════════════════╗\n"
                  f"║  Producto ID: {producto.id}                                          ║\n"
                  "╠═════════════════════════════════════════════════════════════════════╣\n"
                  f"║  Nombre: {producto.nombre}                                          ║\n"
                  f"║  Descripción: {producto.descripcion}                                ║\n"
                  f"║  Precio: ${producto.precio}                                         ║\n"
                  f"║  Cantidad: {producto.cantidad}                                      ║\n"
                  f"║  Categoría: {producto.categoria}                                    ║\n"
                  "╚═════════════════════════════════════════════════════════════════════╝\n" 
                  + Style.RESET_ALL
            )
    else:
        print(Fore.RED +
              "\n╔══════════════════════════════════════════════════════════════════════════╗\n"
              f"║  ❌  No hay productos de la categoría ingresada.  ❌                      ║\n"
              "╚════════════════════════════════════════════════════════════════════════════╝\n" 
              + Style.RESET_ALL)
     
def validar_opcion(opcion):
    while opcion < 1 or opcion > 8:
        print(f"{Fore.RED}\nLa opción ingresada {opcion}, es inválida, por favor vuelva a ingresar una opción entre 1-8\n{Style.RESET_ALL}")
        opcion = int(input(f"{Fore.GREEN}\nVuelva a ingresar la opción (1-8): {Style.RESET_ALL}"))
    return opcion

def validar_precio(precio):
    while precio < 1:
        print(f"{Fore.RED}\nEl precio ingresado es inválido\n{Style.RESET_ALL}")
        precio = float(input(f"{Fore.GREEN}\nVuelva a ingresar el precio: {Style.RESET_ALL}"))
    return precio

def validar_cantidad(cantidad):
    while cantidad < 1:
        print(f"{Fore.RED}\nLa cantidad ingresada {cantidad} es inválida\n{Style.RESET_ALL}")
        cantidad = int(input(f"{Fore.GREEN}\nVuelva a ingresar la cantidad: {Style.RESET_ALL}"))
    return cantidad

def elegir_campo():
    menu_campo()
    opcion = int(input(f"{Fore.BLUE}\nElija una opción: {Style.RESET_ALL}"))
    while opcion < 1 or opcion > 3:
        print(f"{Fore.RED}\nOpción ingresada {opcion} inválida")
        menu_campo()
        opcion = int(input(f"{Fore.BLUE}\nElija nuevamente una opción: {Style.RESET_ALL}"))
    return opcion

def menu_campo():
    print(Style.BRIGHT + Fore.CYAN +
        """
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║           🛍️  SELECCIONE EL CAMPO POR EL QUE DESEA BUSCAR UN PRODUCTO   🛍️ ║
║                                                                            ║
║           1️⃣  ID                                                           ║
║           2️⃣  Nombre                                                       ║
║           3️⃣  Categoría                                                    ║
║                                                                            ║
║           📝  Ingrese el número de su elección y presione Enter            ║
║                                                                            ║
╚══════════════════════════════════════════════════════════════════════════╝
""" + Style.RESET_ALL
    )

def validar_id(id):
    while id < 1:
        print(f"{Fore.RED}\nEl ID ingresado {id} es inválido.{Style.RESET_ALL}")
        id = int(input(f"{Fore.GREEN}\nIngrese nuevamente un ID válido. (ID > 0)"))
    return id

# Método para convertir una cadena ingresada a minúscula y luego que su primera letra sea mayúscula.
def convertir_palabra_correcta(palabra):
    palabra = palabra.lower()
    palabra = palabra.capitalize()
    return palabra