"""
Programar en Python un generador de contraseñas aleatorio.
Por: María Ríos. Para: Programación V-UBA
"""
from random import sample

def generador(longitud):
    """
    missing funtion or method docstring
    """
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    mayusculas = minusculas.upper()
    numeros = "0123456789"
    simbolos = "@*;/,_-+¡?¿&%$#°|"
    
    secuencia = minusculas + mayusculas + numeros + simbolos
    #sample selecciona de la secuendica la cantidad de elementos que indique logitud
    union = sample(secuencia, longitud)
    resultado ="".join(union)
    #se retorna la contraseña aleatoria
    return resultado
#se indica la longitud
password = generador(10)

print("Contraseña:", password)