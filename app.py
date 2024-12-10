import interfaz.vista as vista
import dao.crud as crud

if __name__ == "__main__":
    crud.crear_tabla_producto() 
    while True:
        vista.mostrar_menu()
        opcion = vista.ingresar_opcion()
        if opcion == 1:
            vista.registrar_un_producto()
        elif opcion == 2:
            vista.buscar_producto()
        elif opcion == 3:
            vista.mostrar_productos()
        elif opcion == 4:
            vista.actualizar_producto()
        elif opcion == 5:
            vista.eliminar_producto()
        elif opcion == 6:
            vista.reportar_bajo_stock()
        elif opcion == 7:
            vista.listar_productos_categoria()
        elif opcion == 8:
            break