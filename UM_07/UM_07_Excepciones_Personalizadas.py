"""
assert es una palabra clave para realizar afirmaciones o 
comprobaciones de condiciones.
assert expresion , mensaje_de_error
"""

try:
    edad= int(input("Ingrese la edad:"))
    assert edad>=0, "Error: la edad no puede ser negativa"
    print(f"edad ingresada correctamente {edad}")
except (ValueError ,AssertionError) as e:
    print(f"{e}")   


