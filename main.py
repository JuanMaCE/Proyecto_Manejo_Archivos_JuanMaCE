import os
import datetime


def leer_archivo_binario(ruta_archivo):
    with open(ruta_archivo, 'rb') as archivo:
        version = archivo.read(6)
        print(version)
        weight_size = int.from_bytes(archivo.read(2), 'little')
        height_size = int.from_bytes(archivo.read(2), 'little')
        print(weight_size, height_size)
        number_of_colors = int.from_bytes(archivo.read(1), 'little')
        print(number_of_colors)
        print(" LZW (Lempel-Ziv-Welch)")
        print("little-endian")
        color_of_background = int.from_bytes(archivo.read(1), 'little')
        print(color_of_background)
        cantidad_imagenes = 0
        while True:
            bloque = archivo.read(1)
            if not bloque:
                break  # Final del archivo
            if bloque == b'\x2C':  # Bloque de imagen
                cantidad_imagenes += 1
            elif bloque == b'\x3B':  # Final del archivo GIF
                break
        print(cantidad_imagenes)
        fecha_creacion = datetime.datetime.fromtimestamp(os.path.getctime(ruta_archivo))
        fecha_modificacion = datetime.datetime.fromtimestamp(os.path.getmtime(ruta_archivo))
        print(fecha_creacion)
        print(fecha_modificacion)


ruta = "earth.gif"
leer_archivo_binario(ruta)
