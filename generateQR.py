import qrcode  # Importamos el modulo necesario para trabajar con codigos QR
imagen = qrcode.make('Hola mundo!')  # Creamos un codigo a partir de una cadena de texto
archivo_imagen = open('codigo.png', 'wb')
img.save(archivo_imagen)
archivo_imagen.close()