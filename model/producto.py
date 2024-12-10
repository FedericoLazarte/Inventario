from colorama import Fore, Style # type: ignore

class Producto:
    def __init__(self, nombre, descripcion, precio, cantidad, categoria, id = None):
        self.__validar_no_negativo(precio, "El precio")
        self.__validar_no_negativo(cantidad, "La cantidad")
        self.__id = id
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__cantidad = cantidad
        self.__categoria = categoria

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def descripcion(self):
        return self.__descripcion
    
    @property
    def precio(self):
        return self.__precio
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @property
    def categoria(self):
        return self.__categoria
    
    @precio.setter
    def cambiar_precio(self, nuevo_precio):
        self.__validar_no_negativo(nuevo_precio, "El nuevo precio")
        self.__precio = nuevo_precio
    
    @cantidad.setter
    def cambiar_cantidad(self, nueva_cantidad):
        self.__validar_no_negativo(nueva_cantidad, "La nueva cantidad")
        self.__cantidad = nueva_cantidad

    def __str__(self):
        return f"{Fore.BLUE}ID: {self.id}\nNombre del Producto: {self.nombre}\nPrecio del Producto {self.precio}\nCantidad: {self.cantidad}\nCategoría: {self.categoria}\n{Style.RESET_ALL}"

   
    def __validar_no_negativo(self, valor, mensaje):
        if valor < 0:
            raise ValueError(f"{mensaje} no puede ser negativo.")

    def __validar_menor_o_igual(self, valor, limite, mensaje):
        if valor > limite:
            raise ValueError(mensaje)