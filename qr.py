"""
Programar en Python un generador de códigos qr personalizados (tamaño y color definidos por el usuario), el qr debe enlazar a la url de Python
Por: María Ríos. Para: Programación V-UBA
"""
import qrcode
# Obtener tamaño y color del usuario por terminal
url = "https://www.python.org/"
tamaño = int(input("Ingrese el tamaño (1-40) "))
color_frontal = input("Ingrese el color del frente del QR (en ingles): ").strip().lower()
color_fondo = input("Ingrese el color de fondo del QR (en ingles): ").strip().lower()

# Crear un objeto QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,# Nivel de corrección de errores
    box_size=tamaño,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Crear una imagen del código QR con el color especificado
qr_image = qr.make_image(fill_color=color_frontal, back_color=color_fondo)

# Guardar la imagen
qr_image.save("codigo_qr.png")
