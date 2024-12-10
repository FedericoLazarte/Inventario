# Sistema de Inventario de Productos

Este es un sistema para gestionar productos de un inventario, donde podremos registrar, actualizar, eliminar y consultar productos. El sistema está diseñado para realizar operaciones como agregar nuevos productos al inventario, buscarlos mediante distintos campos, actualizar el stock, su eliminación y llevar a cabo reportes sobre un stock específicado.

## Características

- **Registrar Producto**: Permite registrar un nuevo producto con diferentes detalles, tales como nombre, descripción, precio, cantidad y categoría.
- **Mostrar Producto**: Permite consultar un producto específico mediante su ID, nombre o categoría (en el caso de catgoría, se queda con el primer encuentro).
- **Mostrar todos los Productos**: Muestra todos los productos registrados en el sistema.
- **Actualizar el producto**: Permite actualizar la cantidad de un producto especificado por su ID.
- **Eliminar Producto**: Permite eliminar un producto mediante su ID.
- **Reportar Bajo Stock**: Muestra los productos cuyo stock está por debajo de una cantidad mínima.
- **Listar Productos por Categoría**: Permite listar todos los productos de una categoría específica.

## Requisitos

- Python 3.x
- `Colorama` para la gestión de colores en la terminal.

## Estructura del proyecto

- `dao/crud.py`: Contiene las funcione CRUD (crear, leer, actualizar, eliminar) para interactuar con la base de datos.
- `model/producto.py`: Define la clase `Producto` que representa los productos del sistema.
- `interfaz/vista.py`: Define la interfaz del usuario con los diferentes menús y opciones de interacción.
- `app.py`: Clase donde se ejecutará la aplicación.

## Funciones Principales

1. `registrar_un_producto()`: Registra un nuevo producto en el sistema, validando que no exista un producto con el mismo nombre.
2. `buscar_producto()`: Permite buscar un producto específico, mediante su ID, nombre o categoría (con respecto a categoría se queda con la primera coincidencia).
3. `mostrar_productos()`: Muestra una lista de todos los productos registrados en el sistema.
4. `actualizar_producto()`: Actuliza la cantidad de un producto específicado mediante su ID.
5. `eliminar_producto()`: Elimina un producto del sistema mediante su ID.
6. `reportar_bajo_stock()`: Permite ver los productos cuya cantidad es menor a una cantidad específica ingresada por el usuario.
7. `listar_productos_categoria()`: Muestra todos los productos de una categoría específica.

## Contacto

- **Email**: <fedelazarte2015@gmail.com>
