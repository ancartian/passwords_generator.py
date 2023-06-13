"""
Generador de contraseñas seguras y aleatorias.
"""

import random
import string

def generar_contrasena(longitud):
    """Genera una contraseña aleatoria."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

# Ejemplo de uso:
longitud = 10
contrasena_generada = generar_contrasena(longitud)
print("Contraseña generada:", contrasena_generada)
