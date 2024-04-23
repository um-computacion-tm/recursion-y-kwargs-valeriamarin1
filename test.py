import unittest

def buscar_datos(*args, **kwargs):
    if len(args) != 4:
        print("Debe proporcionar exactamente cuatro argumentos: primer_nombre, segundo_nombre, primer_apellido, segundo_apellido")
        return None
    
    for key, value in kwargs.items():
        if all(value.get(attr) == arg for arg, attr in zip(args, ["primer_nombre", "segundo_nombre", "primer_apellido", "segundo_apellido"])):
            return key
    
    print("No se encontraron coincidencias en la base de datos.")
    return None

class TestBuscarDatos(unittest.TestCase):

    def setUp(self):
        self.database = {
            "persona1": {
                "primer_nombre": "Pablo",
                "segundo_nombre": "Diego",
                "primer_apellido": "Ruiz",
                "segundo_apellido": "Picasso"
            }
        }

    def test_buscar_persona_existente(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **self.database)
        self.assertEqual(resultado, "persona1")

    def test_argumentos_insuficientes(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz", **self.database)
        self.assertIsNone(resultado)

    def test_argumentos_excesivos(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", "Extra", **self.database)
        self.assertIsNone(resultado)

    def test_buscar_persona_inexistente(self):
        resultado = buscar_datos("juan", "José", "Arcila", "López", **self.database)
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()


