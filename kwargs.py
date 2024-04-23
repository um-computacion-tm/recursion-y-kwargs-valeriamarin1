def buscar_datos(*args, **kwargs):
    for key, value in kwargs.items():
        if all(arg in value.values() for arg in args):
            return key
    return None

# Ejemplo de uso
database = {
    "1": {"nombre": "Pablo", "segundo_nombre": "Diego", "apellido_paterno": "Ruiz", "apellido_materno": "Picasso"},
    "2": {"nombre": "Otro", "segundo_nombre": "Nombre", "apellido_paterno": "Apellido", "apellido_materno": "Distinto"}
}

resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
print(resultado)  # Debería imprimir 1



